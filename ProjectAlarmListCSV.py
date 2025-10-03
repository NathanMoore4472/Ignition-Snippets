import system # type: ignore

# PRINT ALL ALARMS IN A GIVEN PATH AND CREATE A CSV THAT IS SAVED TO DISK
# HEADINGS: NAME, LABEL, PRIORITY, TAGPATH

search_path = '[US_GRX01]GRX01/0165_Mem/CDP-AIML 1/FB01'

filter__obj = {"recursive":True}
data = []
	
udt = system.tag.browse(search_path, filter__obj).results

for tag in udt:
	fullPath = str(tag['fullPath'])
	config = system.tag.getConfiguration(fullPath)[0]
	enabled = system.tag.read(fullPath + '.enabled').value
	
	try: 
		if enabled and config.get("alarms", None) is not None:
			for index, alarm in enumerate(config['alarms']):
				alarmName = config['alarms'][index]['name']
				
				Name = system.tag.read(fullPath + '.Documentation').value
				priority = system.tag.read(fullPath + '/Alarms/' + alarmName + '.priority').value			
				label = system.tag.read(fullPath + '/Alarms/' + alarmName + '.label').value

				row = [Name, label, priority, fullPath]
				print(row)
				data.append(row)
	except Exception as e:
		print('Errored: ' + str(e))
		
headers = ['Name', 'Label', 'Priority', 'Tag Path']
ds = system.dataset.toDataSet(headers, data)

csv = system.dataset.toCSV(ds)
system.file.writeFile("/Users/nathan/Desktop/Alarm List.csv", csv)