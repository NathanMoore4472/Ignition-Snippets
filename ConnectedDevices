import system # type: ignore

# CREATE ARRAY OF DEVICE CONNECTED TAG PATHS

def connectedDevicesBrowse(path, filter):
	global pendingCall
	results = system.tag.browse(path,filter) 
	for result in results.getResults():
		if str(result['tagType']) == "UdtInstance" and "Device" in str(result['typeId']):
			resultList.append(str(result['fullPath']) + '/Comms/Connected')
			pendingCall += 1
			connectedDevicesBrowse(result['fullPath'], filter)
		if str(result['tagType']) == "Folder":
			pendingCall += 1
			connectedDevicesBrowse(result['fullPath'], filter)
		if str(result['tagType']) == "UdtInstance" and "Systems" in str(result['typeId']):
			pendingCall += 1
			connectedDevicesBrowse(result['fullPath'], filter)
	pendingCall -= 1
	if pendingCall == 0:
		return resultList
#main
resultList = []
#counter to detect end of browse function
global pendingCall
pendingCall = 1
BuildingName=system.tag.read("_Core/BuildingName").value 
myTags = connectedDevicesBrowse(BuildingName,{})

paths = []
for tag in myTags:
	res = system.tag.read(tag)  
	if res.quality.getName() == 'Bad_Disabled' or res.quality.getName() == 'Bad_NotFound':
		pass
	else:
		paths.append(tag)
		
system.tag.write('_Core/allDevicePaths', paths) 

# READ THROUGH DEVICE PATHS AND UPDATE CONNECTED PERCENTAGE

connectedDevices = 0.0
disconnectedDevices = 0.0

paths = system.tag.read("_Core/allDevicePaths").value 

for path in paths:
	res = system.tag.read(path) 
	if res.quality.getName() == 'Bad_Disabled' or res.quality.getName() == 'Bad_NotFound':
		pass
	else:
		if res.value:
			connectedDevices += 1
		else:
			disconnectedDevices += 1	
total = connectedDevices + disconnectedDevices

print(total)
print(connectedDevices)

percentage = (connectedDevices / total) * 100

system.tag.writeBlocking("_Core/Infrastructure/System/Percent of Devices Online", percentage)