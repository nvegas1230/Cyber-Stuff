import xml.etree.ElementTree as xmlRead
import os

main = xmlRead.parse("notes_folder/main.xml")
root = main.getroot()
currentPath = root
currentFile = main
running = True

def createXmlFile(path, text, filename):
  if path is None:
    root = xmlRead.Element(filename)

    child = xmlRead.SubElement(root, "child")
    child.text = text

    tree = xmlRead.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"XML file '{filename}' created with the given text.")
def addTextToXml(path, text):
  try:
    tree = xmlRead.parse(path)
    root = tree.getroot()

    new_child = xmlRead.SubElement(root, "child")
    new_child.text = text

    tree.write(path, encoding="utf-8", xml_declaration=True)
    print(f"New text added to '{path}'.")
  except Exception as e:
    print(f"Error: {e}")
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
  if path.tag != "root":
    element_names+="up"
  print("Children of element: "+element_names.strip())
def elementPath(tag):
  global currentPath
  if tag == "up":
    pathUp()
  elif tag is not None:
    newPath = currentPath.find(tag)
    currentPath = newPath
def listAction():
  global currentPath
  actionsList = "Actions: exit"
  for element in currentPath:
    if element is not None:
      actionsList = actionsList + ", cd, ls"
      break
  if currentPath.text.strip() != "":
    actionsList = actionsList + ", gettext"
  print(actionsList)
def action():
  global currentPath
  global root
  if currentPath is None:
    currentPath = root
    print("Path is invalid: reset to default")
  print("\nYour current path is: "+currentPath.tag)
  action = input("Input action: ").strip()
  print()
  if action == "":
    return
  elif action == "exit":
    print("Exiting...")
    return action
  elif action == "ls":
    getElementNames(currentPath)
  elif action == "cd":
    path = input("Input directory/element: ").strip()
    if path == "up":
      pathUp()
    elif path.strip() == "":
      return
    else:
       elementPath(path)
  elif action == "gettext":
    print(currentPath.text)
  elif action == "help":
    listAction()
  else:
    elementPath(action)
while running:
  result = action()
  if result == "exit":
    running = False