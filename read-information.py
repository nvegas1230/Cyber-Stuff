import xml.etree.ElementTree as xmlRead
import tkinter as tk

main = xmlRead.parse("test.xml")
root = main.getroot()
currentPath = root
running = True
def parentLoop(pathGiven):
  global currentPath
  check = None
  for element in pathGiven:
    if element.tag == currentPath.tag:
      currentPath = pathGiven
      break
    else:
      parentLoop(element)
  return check
def pathUp():
  global currentPath
  parentTest = parentLoop(root)
  if parentTest is not None:
    elementPath(parentTest)
def getElementNames(path):
  element_names = ""
  if path is not None:
    for child in path:
      element_names += child.tag + ", "
  element_names+="up"
  print("Children of element: "+element_names.strip())
def elementPath(tag):
  if tag == "up":
    return 
  if tag is not None:
    newPath = currentPath.find(tag)
    return newPath
def action():
  global currentPath
  print("\nYour current path is: "+currentPath.tag)
  print("Actions: exit, cd, ls, gettext")
  action = input("Input action: ").strip()
  print()
  if action == "exit":
    print("Exiting...")
    return action
  elif action == "ls":
    getElementNames(currentPath)
  elif action == "cd":
    path = input("Input directory/element: ").strip()
    if path == "up":
      pathUp()
    else:
      currentPath = elementPath(path)
  elif action == "gettext":
    print(currentPath.text)
while running:
  result = action()
  if result == "exit":
    running = False