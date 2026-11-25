tags = system.tag.browse('[default]root/folder1/child/tag', filter={})

for tag in tags:
	tagPath = tag['fullPath']
  print tagPath.toString()  # prints '[default]root/folder1/child/tag'
  print tagPath.toStringPartial() # prints 'root/folder1/child/tag'
  print tagPath.getSource() rawdataPC # prints 'default'

