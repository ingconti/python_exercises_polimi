import xml.etree.ElementTree as ET
import pandas as pd

LIST_OF_SERVICES = "index.xml"

def parse(node):
	return ""

def getListOfServices():
	xml_tree = ET.parse(LIST_OF_SERVICES)
	xroot = xml_tree.getroot()

	#columns = []
	for node in xroot: # only one.. anyway..
		#print(node.attrib)
		for field in node:
			#print(field)
			attrib = field.attrib
			#label = attrib['Label']
			#print(attrib)
			d = dict(attrib)
			label = attrib.get('Label')
			print(label)
			#text = field.text
			#print(text)
			if label == "GHO":
				parse(d)

	print("----")

#main code:
getListOfServices()



