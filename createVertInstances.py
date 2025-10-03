import time

start = time.time()

cacheTagData = [
    [
        "Current",
        [
            [
                "_items",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Current/B",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Current/C",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Current/Ground",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Current/Neutral",
                        "quality": "Good",
                        "value": 0,
                    },
                ],
            ]
        ],
    ],
    [
        "Energy",
        [
            [
                "Active",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Energy/Active/Energy",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Energy/Active/From Load",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Energy/Active/To Load",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Energy/Active/Total",
                        "quality": "Good",
                        "value": 0,
                    },
                ],
            ],
            [
                "Apparent",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Energy/Apparent/Energy",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Energy/Apparent/From Load",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Energy/Apparent/To Load",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Energy/Apparent/Total",
                        "quality": "Good",
                        "value": 0,
                    },
                ],
            ],
        ],
    ],
    [
        "Misc Folder",
        [
            [
                "_items",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Misc Folder/Device Time",
                        "quality": "Good",
                        "value": None,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Misc Folder/Faceplate Name",
                        "quality": "Good",
                        "value": None,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Misc Folder/Legacy Name",
                        "quality": "Good",
                        "value": None,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Misc Folder/Richards Special Feature",
                        "quality": "Uncertain_InitialValue",
                        "value": None,
                    },
                ],
            ]
        ],
    ],
    [
        "Power",
        [
            [
                "Active",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Active/A",
                        "quality": "Good",
                        "value": 2,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Active/Average",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Active/B",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Active/C",
                        "quality": "Good",
                        "value": 0,
                    },
                ],
            ],
            [
                "Apparent",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Apparent/A",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Apparent/Average",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Apparent/B",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Apparent/C",
                        "quality": "Good",
                        "value": 0,
                    },
                ],
            ],
            [
                "Demand",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Demand/Active Power",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Demand/Apparent Power",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Demand/Interval",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Demand/Last Reset",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Demand/Peak Active Power",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Demand/Peak Apparent Power",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Demand/Peak Power",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Demand/Peak Reactive Power",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Demand/Reactive Power",
                        "quality": "Good",
                        "value": 0,
                    },
                ],
            ],
            [
                "Factor",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Factor/A",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Factor/Average",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Factor/B",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Factor/C",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Factor/Lead Lag",
                        "quality": "Good",
                        "value": 0,
                    },
                ],
            ],
            [
                "Reactive",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Reactive/A",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Reactive/Average",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Reactive/B",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Power/Reactive/C",
                        "quality": "Good",
                        "value": 0,
                    },
                ],
            ],
        ],
    ],
    [
        "Voltage",
        [
            [
                "_items",
                [
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Voltage/A-B",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Voltage/A-N",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Voltage/Average",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Voltage/Average-N",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Voltage/B-C",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Voltage/B-N",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Voltage/C-A",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Voltage/C-N",
                        "quality": "Good",
                        "value": 0,
                    },
                    {
                        "path": "[US.PRZ.05.AZ06.E]DCIS/US/PRZ/05/01/1301/New Instance/Voltage/Frequency",
                        "quality": "Good",
                        "value": 0,
                    },
                ],
            ]
        ],
    ],
]


columnCount = 3
maxItems = 14

instances = [{"buckets": [], "heightEst": 0} for _ in range(columnCount)]

for folder in cacheTagData:
    folderName = folder[0]
    subBuckets = folder[1]

    # Copy subBuckets to work with a fresh list
    remainingBuckets = [list(bucket) for bucket in subBuckets]

    while remainingBuckets:
        # Start a new page
        tagsThisPage = 0
        tags = []
        placedIndices = []

        # Try to pack as many full subBuckets as fit
        for i, bucket in enumerate(remainingBuckets):
            subBucketName, items = bucket[0], bucket[1]

            # Only allow if this entire subBucket will fit in the current page
            if len(items) + tagsThisPage <= maxItems:
                # The filtering out of disabled tags is now done in cacheTagData
                # validTags = [tag.path for tag in items if tag.quality != 'Bad_Disabled']
                validTags = [tag.get("path", "") for tag in items]
                tags += validTags
                tagsThisPage += len(validTags)
                placedIndices.append(i)

        # Place subBuckets
        if tags:
            placeCol = min(instances, key=lambda col: col["heightEst"])
            placeCol["buckets"].append({"name": folderName, "paths": tags})
            placeCol["heightEst"] += (len(tags) + 1) * 25  # height estimate
        else:
            # No subBucket could fit: force move largest one to next page
            # Prevent infinite loop on oversized buckets
            bucket = remainingBuckets.pop(0)
            subBucketName, items = bucket[0], bucket[1]
            validTags = [tag.get("path", "") for tag in items]

            placeCol = min(instances, key=lambda col: col["heightEst"])
            placeCol["buckets"].append({"name": folderName, "paths": validTags})
            placeCol["heightEst"] += (len(validTags) + 1) * 25
            continue

        # Remove placed subBuckets from remaining
        for i in reversed(placedIndices):
            del remainingBuckets[i]

print(instances)
