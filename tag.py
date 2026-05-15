"""
tag.py - Modern Ignition 8.1 tag navigation with dot-notation access
=====================================================================
Inspired by pturmel's original shared.tag module (automation-pros.com),
rewritten for Ignition 8.1 using system.tag.browse / system.tag.readBlocking.

Works in all scopes: Gateway, Perspective, Vision, Designer.

Usage
-----
Place in a project script library (e.g. shared.tag)

    from shared import tag

    # Wrap any tag path
    root = tag.node("[default]Devices/Chiller_01")
    # or
    root = tag.TagNode("[default]Devices/Chiller_01")

    # Read a child tag value via dot notation
    print root.RunStatus.value
    print root.Setpoints.SupplyTemp.value

    # Write a value
    root.Setpoints.SupplyTemp.value = 12.5

    # Check quality
    qv = root.RunStatus.qualified_value
    print qv.quality

    # Get the full resolved path of any node
    print root.Setpoints.SupplyTemp.path

    # Iterate over children
    for child in root.children:
        print child.name, child.path

    # Force a cache refresh (e.g. after tag structure changes)
    root.refresh()

Notes
-----
- Children are discovered via system.tag.browse on first attribute access,
  then cached. Subsequent accesses to the same child do NOT re-browse.
- Values are NOT cached — every .value access calls readBlocking.
- Call .refresh() on any node to clear its child cache and re-browse.
- Tag names that clash with Python builtins or TagNode attributes (e.g.
  'value', 'path', 'name') can be accessed with subscript notation:
      root["value_tag_named_value"]
- Names are stored and looked up case-insensitively, matching Ignition's
  own behaviour. The original casing is preserved in .name / .path.
"""

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _browse_children(tag_path):
    """
    Return a list of (name, fullPath, isLeaf) tuples for direct children
    of tag_path. Uses system.tag.browse which returns BrowseResults.
    """
    results = system.tag.browse(tag_path, {})
    children = []
    for result in results.getResults():
        name     = str(result.get("name", ""))
        fullPath = str(result.get("fullPath", ""))
        tagType  = str(result.get("tagType", ""))
        # Folders, UDT instances, and UDT definitions are non-leaf (navigable)
        is_leaf  = tagType not in ("Folder", "UdtInstance", "UdtType")
        children.append((name, fullPath, is_leaf))
    return children


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

class TagNode(object):
    """
    A lazy, caching wrapper around an Ignition tag path that supports
    dot-notation traversal of the tag tree.

    Leaf tags expose .value (read/write) and .qualified_value (read-only).
    Non-leaf tags (folders, UDT instances) return child TagNode objects.
    """

    # Class-level shared cache: path (str) -> list of (name, fullPath, isLeaf)
    # This persists for the lifetime of the Jython interpreter session,
    # effectively surviving across multiple script calls until gateway restart
    # or an explicit .refresh() call.
    _cache = {}

    def __init__(self, path, name=None):
        # Normalise: strip trailing slash
        self._path = path.rstrip("/")
        self._name = name or self._path.rsplit("/", 1)[-1]

    # ------------------------------------------------------------------
    # Core properties
    # ------------------------------------------------------------------

    @property
    def path(self):
        """Full tag path including provider, e.g. [default]Devices/Chiller/Run"""
        return self._path

    @property
    def name(self):
        """Tag name (last path segment)."""
        return self._name

    @property
    def value(self):
        """Read the current tag value (blocking, uses quality-value pair)."""
        qvs = system.tag.readBlocking([self._path])
        return qvs[0].value

    @value.setter
    def value(self, new_value):
        """Write a value to this tag."""
        system.tag.writeBlocking([self._path], [new_value])

    @property
    def qualified_value(self):
        """Return the full QualifiedValue (value, quality, timestamp)."""
        return system.tag.readBlocking([self._path])[0]

    @property
    def children(self):
        """
        Return a list of TagNode objects for all direct children.
        Results are cached per path.
        """
        return [
            TagNode(full_path, child_name)
            for child_name, full_path, _ in self._get_cached_children()
        ]

    # ------------------------------------------------------------------
    # Cache management
    # ------------------------------------------------------------------

    def _get_cached_children(self):
        if self._path not in TagNode._cache:
            TagNode._cache[self._path] = _browse_children(self._path)
        return TagNode._cache[self._path]

    def refresh(self):
        """
        Clear the child cache for this node (and all descendants).
        Call this if the tag structure has changed at runtime.
        """
        keys_to_remove = [k for k in TagNode._cache if k.startswith(self._path)]
        for k in keys_to_remove:
            del TagNode._cache[k]

    @classmethod
    def clear_all_caches(cls):
        """Wipe the entire class-level cache. Useful after tag imports."""
        cls._cache.clear()

    # ------------------------------------------------------------------
    # Dot-notation and subscript traversal
    # ------------------------------------------------------------------

    def __getitem__(self, item):
        """
        Access a child by name (case-insensitive).
        Returns a TagNode for the child, whether leaf or non-leaf.
        Raises KeyError if the child does not exist.
        """
        lookup = item.lower()
        for child_name, full_path, _ in self._get_cached_children():
            if child_name.lower() == lookup:
                return TagNode(full_path, child_name)
        raise KeyError(
            "No child tag '{}' found under '{}'. "
            "Available: {}".format(
                item,
                self._path,
                [c[0] for c in self._get_cached_children()]
            )
        )

    def __getattr__(self, attr):
        """
        Intercept attribute access for tag child traversal.
        Attributes starting with '_' or matching known Python internals
        are excluded to avoid infinite recursion.
        """
        # Guard: skip private/dunder names and our own known attributes
        if attr.startswith("_"):
            raise AttributeError(attr)
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(
                "'TagNode' has no attribute '{}' and no child tag '{}' "
                "was found under '{}'.".format(attr, attr, self._path)
            )

    # ------------------------------------------------------------------
    # Iteration
    # ------------------------------------------------------------------

    def __iter__(self):
        """Iterate over direct children as TagNode objects."""
        return iter(self.children)

    def __len__(self):
        """Number of direct children."""
        return len(self._get_cached_children())

    # ------------------------------------------------------------------
    # String representations
    # ------------------------------------------------------------------

    def __repr__(self):
        return "TagNode('{}')".format(self._path)

    def __str__(self):
        """
        Attempt to return the tag's current value as a string.
        Falls back to the path if the read fails or the tag is non-leaf.
        """
        try:
            return str(self.value)
        except Exception:
            return self._path


# ---------------------------------------------------------------------------
# Convenience factory — mirrors pturmel's original module-level entry point
# ---------------------------------------------------------------------------

def node(path):
    """
    Convenience function. Returns a TagNode for the given path.

        import shared.tag as tag
        chiller = tag.node("[default]Devices/Chiller_01")
        print chiller.RunStatus.value
    """
    return TagNode(path)
