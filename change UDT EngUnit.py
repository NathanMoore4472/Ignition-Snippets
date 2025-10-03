shared.tools.pretty.install()

path = "[US_PRZ_03_AZ01_E]_types_/1 - MAIN/1 - Elements"
filter = {"recursive": True}

readList = []
engUnitMap = {}

results = system.tag.browse(path, filter)

for res in results.getResults():
    # We only want actual tag nodes (not folders)
    if str(res["tagType"]) == "AtomicTag":
        readList.append(str(res["fullPath"]) + ".EngUnit")

reads = system.tag.readBlocking(readList)

for index, tag in enumerate(reads):
    if tag.quality.isGood():
        engUnit = str(tag.value).strip()
        if engUnit:  # Only if non-empty
            engUnitMap.setdefault(engUnit, []).append(readList[index])


for unit, tags in engUnitMap.iteritems():
    if unit == "gal/hr":
        for tag in tags:
            system.tag.write(tag, "volume/hr")

engUnitMap


""" ################################## TABNINE VERSION ############################# """


def scanUDTEngUnits():
    """
    Scans through all UDT instances in the tag system, extracts EngUnit properties,
    and creates a dictionary mapping EngUnits to arrays of tag paths.
    Uses a single block read for efficiency.

    Returns:
        dict: A dictionary where keys are EngUnit values and values are lists of tag paths
              that have that EngUnit. Example: {"°C": ["/path/to/temp1", "/path/to/temp2"]}
    """
    engUnitDict = {}

    # Get all tags in the system (starting from root)
    allTags = system.tag.browse(
        path="_types_/1 - MAIN/1 - Elements", filter={"recursive": True}
    )

    # Collect all UDT tag paths and their corresponding EngUnit paths
    udtTagPaths = []
    engUnitPaths = []

    for tag in allTags.getResults():
        tagPath = str(tag["fullPath"])
        # Check if this is a UDT instance by looking for typeId
        if str(tag["tagType"]) == "AtomicTag":
            udtTagPaths.append(tagPath)
            engUnitPaths.append(tagPath + ".EngUnit")

    # Single block read for all EngUnit properties
    if engUnitPaths:
        engUnitResults = system.tag.readBlocking(engUnitPaths)

        # Process the results
        for i, engUnitRead in enumerate(engUnitResults):
            tagPath = udtTagPaths[i]
            # Only process if EngUnit exists and has a valid value
            if (
                engUnitRead.quality.isGood()
                and engUnitRead.value is not None
                and str(engUnitRead.value) != ""
            ):
                engUnitValue = str(engUnitRead.value)
                # Initialize the list if this EngUnit hasn't been seen before
                if engUnitValue not in engUnitDict:
                    engUnitDict[engUnitValue] = []

                # Add the tag path to the list for this EngUnit
                engUnitDict[engUnitValue].append(tagPath)

    return engUnitDict


def scanUDTEngUnitsAdvanced(rootPath="", includeDisabled=False):
    """
    Advanced version that scans UDT instances for EngUnit properties with additional options.
    Uses a single block read for efficiency.

    Args:
        rootPath (str): The root path to start scanning from. Empty string scans entire system.
        includeDisabled (bool): Whether to include disabled tags in the scan.

    Returns:
        dict: A dictionary with EngUnit values as keys and dictionaries as values containing:
              - 'tagPaths': list of tag paths with that EngUnit
              - 'count': number of tags with that EngUnit
    """
    engUnitDict = {}

    # Configure browse filter
    browseFilter = {"recursive": True}
    if not includeDisabled:
        browseFilter["tagType"] = "AtomicTag"

    # Get all tags from the specified root path
    allTags = system.tag.browse(path=rootPath, filter=browseFilter)

    # Collect all UDT tag paths and their corresponding EngUnit paths
    udtTagPaths = []
    engUnitPaths = []

    for tag in allTags.getResults():
        tagPath = tag["fullPath"]

        # Check if this is a UDT instance
        if tag.get("typeId"):
            # Skip disabled tags if requested
            if not includeDisabled and not tag.get("enabled", True):
                continue

            udtTagPaths.append(tagPath)
            engUnitPaths.append(tagPath + ".EngUnit")

    # Single block read for all EngUnit properties
    if engUnitPaths:
        try:
            engUnitResults = system.tag.readBlocking(engUnitPaths)

            # Process the results
            for i, engUnitRead in enumerate(engUnitResults):
                tagPath = udtTagPaths[i]

                if engUnitRead.quality.isGood() and engUnitRead.value is not None:
                    engUnitValue = str(engUnitRead.value).strip()

                    # Only process non-empty EngUnit values
                    if engUnitValue:
                        if engUnitValue not in engUnitDict:
                            engUnitDict[engUnitValue] = {"tagPaths": [], "count": 0}

                        engUnitDict[engUnitValue]["tagPaths"].append(tagPath)
                        engUnitDict[engUnitValue]["count"] += 1

        except Exception as e:
            # Log the error if needed for debugging
            system.util.getLogger("UDTScanner").warn(
                "Error during block read: {}".format(str(e))
            )

    return engUnitDict


def scanUDTEngUnitsChunked(rootPath="", includeDisabled=False, chunkSize=1000):
    """
    Version that processes UDTs in chunks to handle very large tag systems.
    Uses block reads but splits into manageable chunks.

    Args:
        rootPath (str): The root path to start scanning from. Empty string scans entire system.
        includeDisabled (bool): Whether to include disabled tags in the scan.
        chunkSize (int): Number of tags to read in each block read operation.

    Returns:
        dict: A dictionary with EngUnit values as keys and lists of tag paths as values.
    """
    engUnitDict = {}

    # Configure browse filter
    browseFilter = {"recursive": True}
    if not includeDisabled:
        browseFilter["tagType"] = "AtomicTag"

    # Get all tags from the specified root path
    allTags = system.tag.browse(path=rootPath, filter=browseFilter)

    # Collect all UDT tag paths and their corresponding EngUnit paths
    udtTagPaths = []
    engUnitPaths = []

    for tag in allTags.getResults():
        tagPath = tag["fullPath"]

        # Check if this is a UDT instance
        if tag.get("typeId"):
            # Skip disabled tags if requested
            if not includeDisabled and not tag.get("enabled", True):
                continue

            udtTagPaths.append(tagPath)
            engUnitPaths.append(tagPath + ".EngUnit")

    # Process in chunks
    for i in range(0, len(engUnitPaths), chunkSize):
        chunkEngUnitPaths = engUnitPaths[i : i + chunkSize]
        chunkUdtPaths = udtTagPaths[i : i + chunkSize]

        try:
            engUnitResults = system.tag.readBlocking(chunkEngUnitPaths)

            # Process the chunk results
            for j, engUnitRead in enumerate(engUnitResults):
                tagPath = chunkUdtPaths[j]

                if engUnitRead.quality.isGood() and engUnitRead.value is not None:
                    engUnitValue = str(engUnitRead.value).strip()

                    # Only process non-empty EngUnit values
                    if engUnitValue:
                        if engUnitValue not in engUnitDict:
                            engUnitDict[engUnitValue] = []

                        engUnitDict[engUnitValue].append(tagPath)

        except Exception as e:
            system.util.getLogger("UDTScanner").warn(
                "Error during chunk read {}-{}: {}".format(i, i + chunkSize, str(e))
            )

    return engUnitDict


def printEngUnitSummary(engUnitDict):
    """
    Prints a formatted summary of the EngUnit dictionary.

    Args:
        engUnitDict (dict): Dictionary returned from scanUDTEngUnits functions
    """
    print("EngUnit Summary:")
    print("=" * 50)

    for engUnit, data in sorted(engUnitDict.items()):
        if isinstance(data, dict):
            # Advanced version format
            print("EngUnit: {} ({} tags)".format(engUnit, data["count"]))
            for tagPath in data["tagPaths"]:
                print("  - {}".format(tagPath))
        else:
            # Simple version format
            print("EngUnit: {} ({} tags)".format(engUnit, len(data)))
            for tagPath in data:
                print("  - {}".format(tagPath))
        print()


# Example usage:
if __name__ == "__main__":
    # Simple scan with single block read
    engUnits = scanUDTEngUnits()
    printEngUnitSummary(engUnits)

    # For very large systems, use the chunked version
    # engUnitsChunked = scanUDTEngUnitsChunked(rootPath="Production", chunkSize=500)
    # printEngUnitSummary(engUnitsChunked)
