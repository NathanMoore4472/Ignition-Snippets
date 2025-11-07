path = '[ProductGW]Vantage'
tags = system.tag.browse(path, {'recursive': True, "tagType":"UdtInstance"})
reads = []

for tag in tags:
	if '1 - Elements' in tag['typeId']:
		continue
	if system.tag.exists(str(tag['fullPath']) + '/Parameters.OPCDeviceName'):
		reads.append(str(tag['fullPath']) + '/Parameters.OPCDeviceName')
		
devices = system.tag.readBlocking(reads)

# Create a set to store unique device names
unique_devices = set()

for i, device in enumerate(devices):
    unique_devices.add(device.value)
    if device.value == '':
    	print reads[i]

# Print unique devices
for device in sorted(unique_devices):  # sorted() is optional, just makes output cleaner
    print device
    
print len(unique_devices)