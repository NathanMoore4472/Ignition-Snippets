provider = 'default'
limit = 10000

query = {
  "options": {
    "includeUdtMembers": True,
    "includeUdtDefinitions": False
  },
  "condition": {
    "tagType": "AtomicTag",
    "attributes": {
      "values": [],
      "requireAll": True
    },
    "valueSource": "opc"
  }
}

# Limited to 100 rows. Use continuationPoint functionality to continue from last result, 
# or remove limit for full results.
results = system.tag.query(provider, query, limit)
rows = []


for tag in results:
	path = str(tag['fullPath'])	
	parent = path[:path.rfind('/')]
	
	server = str(system.tag.read(parent + '/Parameters.OPCServer').value)
	enabled = system.tag.read(path + '.enabled').value
	
	if server != 'Ignition OPC UA Server' or not enabled:
		continue
	
	devicePath = str(system.tag.read(parent + '/Parameters.OPCDeviceName').value)
	deviceParts = devicePath.split(']')
	deviceName = deviceParts[0][1:]
	nodeId = deviceParts[1][:-1]
	
	itemPath = str(system.tag.read(path + '.OPCItemPath').value)
	
	row = [path, deviceName, nodeId, itemPath]
#	print row
	rows.append(row)
	
headers = ['Path','Device','NodeID', 'itemPath']
ds = system.dataset.toDataset(headers, rows)

system.vision.exportCSV('ModbusDeviceMap.csv', True, ds)
