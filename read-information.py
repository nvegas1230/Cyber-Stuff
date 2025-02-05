import xml.etree.ElementTree as xmlRead
import tkinter as tk

main = xmlRead.parse("test.xml")
root = main.getroot()
currentPath = root
running = True

def get_element_names(path):
  element_names = ""
  
  if path is not None:
    for child in path:
      element_names += child.tag + ", "
  element_names+="up"
  return element_names.strip() 
def elementPath(tag):
  if tag is not None:
    newPath = currentPath.find(tag)
    if newPath is not None:
      return newPath
    else:
      return "failed"
def getText(path):
  if path.text is None:
    return "failed"
  else:
    return path.text
def action():
  print("Your current path is: ")
  print("Actions: exit, text, path")
  action = input("Input action: ")
  
  if action == "exit":
    return action

  if action == "path":
    options = get_element_names(currentPath)
    print("options: " + options)
    tag = input("Input element to go to: ")
    if tag is None:
      return
    elif tag is not None:
      check = elementPath(tag)
      print("Path")
while running:
  result = action()
  if result == "exit":
    running = False