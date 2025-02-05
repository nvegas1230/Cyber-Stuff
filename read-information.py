import xml.etree.ElementTree as xmlRead

# Parse the XML file
tree = ET.parse("example.xml")
root = tree.getroot()

# Find the "sentence" element and print its text
sentence = root.find("sentence").text
print(sentence)
