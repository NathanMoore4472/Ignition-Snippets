tags = system.tag.browse('[default]root/folder1/child/tag', filter={})

for tag in tags:
  tagPath = tag['fullPath']
  print tagPath.toString()  # prints '[default]root/folder1/child/tag'
  print tagPath.toStringPartial() # prints 'root/folder1/child/tag'
  print tagPath.getSource() # prints 'default'


from com.inductiveautomation.ignition.common.tags.paths.parser import TagPathParser

tp = TagPathParser.parse("[rawdata]Client/Location/UDT01/011005")

print tp.getSource()        # rawdata
print tp.getItemName()      # 011005
print tp.getParentPath()    # [rawdata]Client/Location/PLC01
print tp.getChildPath("01") # [rawdata]Client/Location/PLC01/011005/01
print tp.getProperty()      # None - this path doesn't point at a property

tpv = TagPathParser.parse("[rawdata]Client/Location/PLC01/011005.Value")
print tpv.getProperty()     # Value
print tpv.toStringPartial() # Client/Location/PLC01/011005 (no source or property)

parent = TagPathParser.parse("[rawdata]Client/Location/PLC01")
child  = TagPathParser.parse("[rawdata]Client/Location/PLC01/011005/01/inner")

print parent.isAncestorOf(child)   # True  - child is somewhere below parent
print child.isAncestorOf(parent)   # False - wrong direction
print parent.isAncestorOf(parent)  # False - Not its own ancestor

from com.inductiveautomation.ignition.common import StringPath

p1 = StringPath.parse("[def]Folder/Sub/Thing")
p2 = StringPath.of("Folder", "Sub", "Thing")  
p3 = StringPath.extend(p1, "Child")

print p1.getPathLength(), p1.getLastPathComponent(), p1.getParentPath() # 3 Thing [def]Folder/Sub
