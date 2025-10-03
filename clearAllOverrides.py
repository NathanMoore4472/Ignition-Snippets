def clearAllOverrides(path):
    """
    Clears all overrides from a tag by exporting its configuration, removing all properties 
    except the name, and reconfiguring the tag with the cleaned configuration.
    
    This function removes all tag overrides (such as value overrides, quality overrides, etc.)
    by exporting the tag configuration, stripping out all properties except the tag name,
    and then reconfiguring the tag with the minimal configuration. This effectively resets
    the tag to its default state without overrides.
    
    Args:
        path (str): The full path to the tag whose overrides should be cleared. 
                   Must be a valid tag path in the format "folder/subfolder/tagname".
    
    Returns:
        None: This function does not return a value. It performs the override clearing
              operation as a side effect by modifying the tag configuration in the system.
    """
    basePath = path[: path.rfind("/")]

    export = system.tag.exportTags(tagPaths=[path])

    json = system.util.jsonDecode(export)

    for override in json:
        if str(override) != "name":
            del json[override]

    system.tag.configure(basePath, tags=json)