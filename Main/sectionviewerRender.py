from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
import createSectionRender
import json
import os


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

def addwindowElements(window, fileData, fileDirectory):
    #Clear all child elements of frame on load
    for child in window.winfo_children():
        child.destroy()

    #List of current files to reference and selectedFile
    sectionFiles = []

    #Create label elements
    l1 = Label(window, text="Current Section: " + fileData['filename'], font=("Arial", 60))
    lb1 = Listbox(window, font=("Arial", 16), width=40)
    b1 = Button(window, text="Open File", font=("Arial", 16), command=lambda: openFile(window, readFile(fileDirectory), lb1, fileDirectory, sectionFiles), width=20)
    b2 = Button(window, text="Add File", font=("Arial", 16), command=lambda: addFile(window, readFile(fileDirectory), lb1, fileDirectory), width=20)
    b3 = Button(window, text="Remove File", font=("Arial", 16), command=lambda: removeFile(window, readFile(fileDirectory), lb1, fileDirectory, sectionFiles), width=20)
    b4 = Button(window, text="Undo", font=("Arial", 16), width=20)
    l2 = Label(window, text="Section Directory: " + fileDirectory, font=("Arial", 16))

    #Set background of elements
    l1['bg'] = "#A9B2AC"
    lb1['bg'] = '#C5DAC1'
    b1['bg'] = '#C5DAC1'
    b2['bg'] = '#C5DAC1'
    b3['bg'] = '#C5DAC1'
    b4['bg'] = '#C5DAC1'
    l2['bg'] = "#A9B2AC"

    #Add elements to grid
    l1.grid(column=0, row=0, padx=0, pady=30, columnspan=3)
    lb1.grid(column = 0, row=1, rowspan=4, pady=0, padx=0)
    b1.grid(column = 1, row=1, padx=0)
    b2.grid(column = 1, row=2, padx=0)
    b3.grid(column = 1, row=3, padx=0)
    b4.grid(column = 1, row=4, padx=0)
    l2.grid(column=0, row=5, pady=30, padx=0, columnspan=3)

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
        listbox.insert(index, file)
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
    os.startfile(file[1])


def addFile(window, data, listBox, fileDirectory):
    #Ask user to choose a file to add to the section
    newFile = askopenfile()

    #Check if user didnt pick a file
    if newFile == None:
        return
    
    #Get current json data and add new data
    data["files"][os.path.basename(newFile.name)] = {"filename": os.path.basename(newFile.name), "filepath": newFile.name}
    fileData = json.dumps(data)

    #Write the data and reload window
    writeFile(fileDirectory, fileData)
    addwindowElements(window, data, fileDirectory)
    
def removeFile(window, data, listbox, fileDirectory, sectionFiles):
    try:
        #Remove the selected file from the listbox
        del data["files"][sectionFiles[listbox.curselection()[0]]]
        fileData = json.dumps(data)

        #Write the data and reload window
        writeFile(fileDirectory, fileData)
        addwindowElements(window, data, fileDirectory)
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

    