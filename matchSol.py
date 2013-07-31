import xlrd
import xlwt
import sys
import xml.etree.cElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom


def add_field(field,name,puzzle):
	sfield = ET.SubElement(field,name)
	sfield.text = puzzle

def prettify(elem):
	"""Return a pretty-printed XML string for the Element.
    """
	rough_string = ElementTree.tostring(elem, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	return reparsed.toprettyxml(indent="  ")

root = ET.Element("root")


bookResults = xlwt.Workbook(encoding="utf-8")

try:
	bookSolved = xlrd.open_workbook("solvable.xls")
	bookSolutions = xlrd.open_workbook("solutions.xls")
except:
	bookSolutions.add_sheet("blank")# add new sheet
	bookSolutions.save("solutions.xls")
	bookSolved.add_sheet("blank")# add new sheet
	bookSolved.save("solvable.xls")

#just in case that no book was found
try:
	sheetResults = bookResults.add_sheet("blank")
	sheetSolutions = bookSolutions.add_sheet("blank")
	sheetSolved = bookSolved.add_sheet("blank")
except:
	pass
#end


sheetSolved = bookSolved.sheet_by_index(0)
sheetSolutions = bookSolutions.sheet_by_index(0)


i = j = k = 0



try:
	while 1:
		val = sheetSolved.cell_value(i,0)
		try:
			while 1:
				if(val == sheetSolutions.cell_value(j,0)):
					field = ET.SubElement(root,"data")
					add_field(field,"puzzle",val)

					try:
						for x in range(1,12):
							sol = sheetSolutions.cell_value(j,x)
							if(sol!=""):
								add_field(field,"sol"+str(x),sol)
					except:
						pass
					
					sheetResults.write(k,0,val)

					if(i<454):
						add_field(field,"diff","A")
					elif(i>=454 and i<908):
						add_field(field,"diff","B")
					else:
						add_field(field,"diff","C")


					list = val.split(" ")

					flag=False

					for u in range(0,len(list)):
						if(int(list[u])>9):
							flag = True
							break
					
					if(flag!=True):
						add_field(field,"type","9")
					else:	
						add_field(field,"type","13")

					k+=1
				j+=1
		except:
			pass
		i+=1
		j=0
except:
	pass


f = open('gameData.xml','w')
f.write(prettify(root))





