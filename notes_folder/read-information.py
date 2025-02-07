import xml.etree.ElementTree as xmlRead
import os

main = xmlRead.parse("notes_folder/main.xml")
root = main.getroot()
currentPath = root
currentFile = "main.xml"
running = True

def defineXmlFile(fileName):
  global currentFile
  root = xmlRead.Element(fileName)
  fileName = fileName + ".xml"
  currentFile = fileName
  tree = xmlRead.ElementTree(root)
  filePath = os.path.join("/home/runner/workspace/notes_folder", fileName)
  tree.write(filePath, encoding="utf-8", xml_declaration=True)
  print(f"XML file '{fileName}' created")
def addTextToXml(text):
  global currentFile
  global currentPath
  try:
    tree = xmlRead.parse("notes_folder/"+currentFile)
    currentPath.text = text
    filePath = os.path.join("/home/runner/workspace/notes_folder", currentFile)
    tree.write(filePath, encoding="utf-8", xml_declaration=True)
    print(f"New text added to '{currentFile}' in '{currentPath}'")
  except Exception as e:
    print(f"Error: {e}")
def addSubElementToXml(elementName):
  global currentFile
  global currentPath
  try:
    tree = xmlRead.parse("notes_folder/"+currentFile)
    xmlRead.SubElement(currentPath, elementName)
    currentPath = elementName
    filePath = os.path.join("/home/runner/workspace/notes_folder", currentFile)
    tree.write(filePath, encoding="utf-8", xml_declaration=True)
    print(f"New element '{elementName}' added to '{currentPath}' in '{currentFile}'")
  except Exception as e:
    print(f"Error: {e}")
def createXmlFile(fileName, text):
  defineXmlFile(fileName)
  addSubElementToXml(text)
  addTextToXml(text)
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
  elif tag == "root":
    currentPath = root
  elif tag is not None:
    newPath = currentPath.find(tag)
    if newPath is None:
      print("Invalid path")
    else:
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
  elif action == "addfile":
    textConfirm = True
    while textConfirm:
      fileName = input("Input file name: ").strip()
      fileText = input("Input text: ").strip()
      if fileName == "" or fileText == "":
        print("One field is invalid, please try again\n")
      else:
        textConfirm = False
    createXmlFile(fileName, fileText)
  else:
    elementPath(action)
while running:
  result = action()
  if result == "exit":
    running = False