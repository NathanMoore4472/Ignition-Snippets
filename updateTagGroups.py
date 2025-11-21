	# Recursive function to check if UDT tags have history enabled
	def checkHistoryEnabled(tagPath):
	    # Browse through the current tag path to get all child tags
	    results = system.tag.browse(tagPath)
	    # Iterate over each result (tag)
	    for result in results.getResults():
	        fullTagPath = result['fullPath']
	        # Get the configuration of the tag
	        tagConfig = system.tag.getConfiguration(fullTagPath, False)[0]
	        # Check if the tag is a UDT instance
	        if 'typeId' in tagConfig and tagConfig['typeId'] is not None:
	            # This is a UDT instance, so now check its member tags
#	            system.tag.write(str(fullTagPath)+".historyProvider",currentValue.value)
	            # Recursively check its children
	            checkHistoryEnabled(fullTagPath)
	        # Check if the tag has history enabled
	        if tagConfig.get('historyTagGroup', None):
	            system.tag.write(str(fullTagPath)+".historyTagGroup", currentValue.value)
	        # If the result has children (but isn't a UDT), continue scanning its children
	        elif result['hasChildren']:
	            checkHistoryEnabled(fullTagPath)
	# Specify the path to the 'GRX01' folder, where your UDTs are located
	udtFolderPath = "_types_/"  # Replace '[default]' with your tag provider name if different
	# Start scanning from the 'GRX01' folder (UDTs within this folder)
	checkHistoryEnabled(udtFolderPath)
