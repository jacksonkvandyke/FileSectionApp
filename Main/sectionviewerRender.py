from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfile

import createSectionRender
import helpRenderer
from microserviceConnection import MicroserviceConnection

import json
import os

#These variables will handle the undo and redo stacks
undoStack = []
redoStack = []

#Undo class: This will do the opposite command the user used to undo their command
class UserAction:
    def __init__(self, data):
        self._data = data

    def getData(self):
        return self._data
    
#Microservice class handle
microservice = MicroserviceConnection()

def createWindow(data, dataDirectory):
    #Loaded json data
    fileData = json.loads(data)
    fileDirectory = dataDirectory
    
    #Create window object
    window = Tk()

    #Specify window constraints
    window.config(width="1000", height="600", bg="#A9B2AC")
    window.title("The Librarian")
    
    #Add window elements
    addwindowElements(window, fileData, fileDirectory)
    
    #Launch window
    window.mainloop()

    #Close the running microservice
    microservice.service.kill()


def addwindowElements(window, fileData, fileDirectory):
    #Clear all child elements of frame on load
    for child in window.winfo_children():
        child.destroy()

    #List of current files to reference and selectedFile
    sectionFiles = []

    #Create label elements
    l1 = Label(window, text="Current Section: " + fileData['filename'], font=("Arial", 60))
    lb1 = Listbox(window, font=("Arial", 16), width=40)
    sb1 = Scrollbar(window)
    b1 = Button(window, text="Open File", font=("Arial", 16), command=lambda: openFile(window, readFile(fileDirectory), lb1, fileDirectory, sectionFiles), width=20)
    b2 = Button(window, text="Add File", font=("Arial", 16), command=lambda: addFile(window, readFile(fileDirectory), lb1, fileDirectory), width=20)
    b3 = Button(window, text="Remove File", font=("Arial", 16), command=lambda: removeFile(window, readFile(fileDirectory), lb1, fileDirectory, sectionFiles), width=20)
    b4 = Button(window, text="Undo", font=("Arial", 16), command=lambda: undoAction(window, fileData, fileDirectory), width=20)
    b5 = Button(window, text="Redo", font=("Arial", 16), command=lambda: redoAction(window, fileData, fileDirectory), width=20)
    l2 = Label(window, text="Section Directory: " + fileDirectory, font=("Arial", 16))
    b6 = Button(window, text="Help", font=("Arial", 16), command=helpRenderer.createWindow)
    b7 = Button(window, text="Save Externally", font=("Arial", 16), command=lambda: SaveExternally(window, fileData, lb1, fileDirectory, sectionFiles),width=20)
    b8 = Button(window, text="Retrieve Externally", font=("Arial", 16), command=lambda: RetrieveExternally(window, fileData, lb1, fileDirectory, sectionFiles), width=20)

    #Set background of elements
    l1['bg'] = '#898980'
    lb1['bg'] = '#C5DAC1'
    sb1['bg'] = '#C5DAC1'
    b1['bg'] = '#C5DAC1'
    b2['bg'] = '#C5DAC1'
    b3['bg'] = '#C5DAC1'
    b4['bg'] = '#C5DAC1'
    b5['bg'] = '#C5DAC1'
    l2['bg'] = "#A9B2AC"
    b6['bg'] = '#C5DAC1'
    b7['bg'] = '#C5DAC1'
    b8['bg'] = '#C5DAC1'

    #Link scrollbar to listbox and add double click functionality
    lb1.bind('<Double-Button-1>', lambda event: openFile(window, readFile(fileDirectory), lb1, fileDirectory, sectionFiles))
    lb1.config(yscrollcommand=sb1.set)
    sb1.config(command = lb1.yview) 

    #Add elements to grid
    l1.grid(column=0, row=0, padx=15, pady=30, columnspan=4)
    lb1.grid(column = 0, row=1, rowspan=7, pady=0, padx=0)
    sb1.grid(column=1, row=1, rowspan=7, sticky="ns")
    b1.grid(column = 2, row=1, padx=0)
    b2.grid(column = 2, row=2, padx=0)
    b3.grid(column = 2, row=3, padx=0)
    b4.grid(column = 2, row=4, padx=0)
    b5.grid(column = 2, row=5, padx=0)
    b6.grid(column = 2, row=8, padx=0)
    b7.grid(column = 2, row=6, padx = 0)
    b8.grid(column = 2, row=7, padx = 0)
    l2.grid(column=0, row=9, pady=30, padx=0, columnspan=5)

    #Add data to listbox
    addDataToListBox(readFile(fileDirectory), lb1, fileDirectory, sectionFiles)

def addDataToListBox(data, listbox, fileDirectory, sectionFiles):
    #Loop through files in current section and add to list box
    try:
        #Check if top section exists
        print(data["files"])
    except:
        #If not, add sections to json
        data["files"] = {}
        writeFile(fileDirectory, json.dumps(data))
        
    files = data["files"]
    index = 0
    for file in files:
        listbox.insert(index, files[file]["filename"])
        sectionFiles.append(file)
        index += 1

    #Check if no files are present
    if (len(files) == 0):
        listbox.insert(0, "No files in current section.")
        sectionFiles.append(None)

def openFile(window, data, listbox, fileDirectory, sectionFiles):
    #Open file chosen by user
    try:
        file = data["files"][sectionFiles[listbox.curselection()[0]]]
        print(file)
    except:
        return
    
    #Run file
    os.startfile(file["filepath"])


def addFile(window, data, listBox, fileDirectory):
    #Ask user to choose a file to add to the section
    newFile = askopenfile()

    #Check if user didnt pick a file
    if newFile == None:
        return
    
    #Add action to userAction stack and clear redo stack
    prevData = json.dumps(data)
    action = UserAction(prevData)
    undoStack.append(action)
    redoStack.clear()
    
    #Get current json data and add new data
    strippedName = os.path.basename(newFile.name).split(".", 1)[0]
    data["files"][os.path.basename(newFile.name)] = {"filename": strippedName, "filepath": newFile.name}
    fileData = json.dumps(data)

    #Write the data and reload window
    writeFile(fileDirectory, fileData)
    addwindowElements(window, data, fileDirectory)
    
def removeFile(window, data, listbox, fileDirectory, sectionFiles):
    try:
        #Add action to userAction stack and clear redo stack
        prevData = json.dumps(data)
        action = UserAction(prevData)
        undoStack.append(action)
        redoStack.clear()

        #Remove the selected file from the listbox
        del data["files"][sectionFiles[listbox.curselection()[0]]]
        fileData = json.dumps(data)

        #Write the data and reload window
        writeFile(fileDirectory, fileData)
        addwindowElements(window, data, fileDirectory)
    except:
        lastAction = undoStack[-1]
        undoStack.remove(lastAction)
        return
    
def undoAction(window, fileData, fileDirectory):
    try:
        #Get last action
        lastAction = undoStack[-1]
        undoStack.remove(lastAction)

        #Add to redostack
        jsonString = json.dumps(fileData)
        redoStack.append(UserAction(jsonString))

        #Convert json data to previous state and update UI
        data = lastAction.getData()
        jsonData = json.loads(data)
        writeFile(fileDirectory, data)
        addwindowElements(window, jsonData, fileDirectory)
        return
    except:
        return
    
def redoAction(window, fileData, fileDirectory):
    try:
        #Get last action
        lastAction = redoStack[-1]
        redoStack.remove(lastAction)

        #Add to undostack
        jsonString = json.dumps(fileData)
        undoStack.append(UserAction(jsonString))

        #Convert json data to previous state and update UI
        data = lastAction.getData()
        jsonData = json.loads(data)
        writeFile(fileDirectory, data)
        addwindowElements(window, jsonData, fileDirectory)
        return
    except:
        return

def readFile(fileDirectory):
    #Read file and return in JSON format
    fileRead = open(fileDirectory, 'r')
    jsonData = json.loads(fileRead.read())
    return jsonData

def writeFile(fileDirectory, data):
    #Write data
    fileWrite = open(fileDirectory, 'w')
    fileWrite.write(data)
    fileWrite.close()

def SaveExternally(window, data, listbox, fileDirectory, sectionFiles):
    # Saves the file externally  to database
    try:
        file = data["files"][sectionFiles[listbox.curselection()[0]]]
        print(file)

        #First start connection
        microservice.ConnectService()

        #Save to database
        microservice.SaveFile(file["filepath"])

        #Display alert window that file was saved
        messagebox.showinfo("The Librarian", "File succesfully saved externally.")
    except:
        return
    
def RetrieveExternally(window, data, listbox, fileDirectory, sectionFiles):
    # Retrieves the file externally  to database
    try:
        file = data["files"][sectionFiles[listbox.curselection()[0]]]
        print(file)

        #First start connection
        microservice.ConnectService()

        #Save to database
        microservice.RetrieveFile(file["filepath"])

        #Display alert window that file was saved
        messagebox.showinfo("The Librarian", "File succesfully retrieved externally.")
    except:
        return

    

    