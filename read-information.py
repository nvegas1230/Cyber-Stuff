import xml.etree.ElementTree as xmlRead
import tkinter as tk
"""
# Parse the XML file
tree = xmlRead.parse("test.xml")
root = tree.getroot()

name = input("What information do you want to read? " )
"""
def get_element_names(xml_file):
  # Parse the XML file
  tree = xmlRead.parse(xml_file)
  root = tree.getroot()

  # Initialize an empty string to hold the names of the child elements
  element_names = ""

  # Check if the parent element exists
  if root is not None:
      # Iterate through each child element of the parent
      for child in root:
          # Add the name of the child element to the string
          element_names += child.tag + " "

  return element_names.strip() 

def get_element_given():
  print("test")
options = get_element_names("test.xml")
print("options: " + options)
respond = input("Input element to go to: ")
