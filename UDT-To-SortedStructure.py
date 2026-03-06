def read_udt_deep(root_path):
    """
    Two-pass UDT walker:
      Pass 1 - recursively build the tree structure and collect all leaf paths
      Pass 2 - bulk readBlocking on all leaves, then map results back
    """
    def get_tag_order(tag_path):
        try:
            order = system.tag.readBlocking([tag_path + ".tagOrder"])[0].value
            if order:
                return {name: i for i, name in enumerate(order)}
        except:
            pass
        return {}

    def build_tree(tag_path, sort_index=-1):
        config = system.tag.getConfiguration(tag_path, recursive=False)[0]
        tag_type = str(config.get("tagType", ""))

        if tag_type in ("UdtInstance", "Folder", "UdtType"):
            children = system.tag.getConfiguration(tag_path, recursive=True)[0].get("tags", [])
            tag_order = get_tag_order(tag_path)
            node = {
                child["name"]: build_tree(
                    tag_path + "/" + child["name"],
                    tag_order.get(child["name"], -1)
                )
                for child in children
            }
            node["sortOrder"] = sort_index  # store parent-assigned index on the branch
            return node
        else:
            leaf_configs[tag_path] = (config, sort_index)
            return tag_path

    def populate_tree(node, bulk_results):
        """Replaces leaf sentinels with the actual tag info dicts."""
        if isinstance(node, dict):
            return {k: populate_tree(v, bulk_results) if k != "sortOrder" else v for k, v in node.items()}
        else:
            # node is a leaf sentinel (the tag path string)
            qv = bulk_results[node]
            cfg, sort_index = leaf_configs[node]
            return {
                "value":       str(qv.value),
                "quality":     str(qv.quality),
#                "ts":          str(qv.timestamp),
                "type":        str(cfg.get("dataType", "Unknown")),
                "engUnit":     cfg.get("engUnit", ""),
#                "opcItemPath": cfg.get("opcItemPath", ""),
                "tagPath":     node,
                "sortOrder":   sort_index,
            }

    # --- Pass 1: build structure, harvest leaf paths and configs ---
    leaf_configs = {}
    tree = build_tree(root_path)

    # --- Pass 2: single bulk read, then populate ---
    leaf_paths = leaf_configs.keys()
    qvs = system.tag.readBlocking(leaf_paths)
    bulk_results = dict(zip(leaf_paths, qvs))

    return populate_tree(tree, bulk_results)
    
read_udt_deep("Test")
