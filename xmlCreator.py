import xml.etree.cElementTree as ET

from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
	"""Return a pretty-printed XML string for the Element.
    """
	rough_string = ElementTree.tostring(elem, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	return reparsed.toprettyxml(indent="  ")


root = ET.Element("root")

doc = ET.SubElement(root, "doc")

for i in range(0,2):
	field = ET.SubElement(doc, "data"+str(i))

	for j in range(0,3):
		sfield = ET.SubElement(field, "subData")
		sfield.set("name", "problem")
		sfield.text = "1 2 3 4"+str(i)


f = open('data.xml','w')

f.write(prettify(root))