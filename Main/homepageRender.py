from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
import createSectionRender
import sectionviewerRender

import aboutRenderer

import json
import os

def createWindow():
    #Create window object
    window = Tk()

    #Specify window constraints
    window.config(width="800", height="600", bg="#A9B2AC")
    window.title("The Librarian")

    #File contents
    fileContents = StringVar(window, "None")
    fileDirectory = StringVar(window, "None")
    addwindowElements(window, fileContents, fileDirectory)
    
    #Launch window
    window.mainloop()

    #Send data to section viewer if possible
    if (fileContents.get() != "None"):
        window.destroy()
        sendData(fileContents, fileDirectory)

def addwindowElements(window, fileContents, fileDirectory):
    #Variables for file validation
    validText = StringVar()

    #Create window elements
    l1 = Label(window, text="The Librarian", font=("Arial", 60))
    b1 = Button(window, text="Create Section", font=("Arial", 32), command=createSectionRender.createWindow, width=15)
    b2 = Button(window, text="Load Section", font=("Arial", 32), command=lambda: loadSection(window, validText, l2, fileContents, fileDirectory), width=15)
    l2 = Label(window, textvariable=validText, font=("Arial", 16))
    b3 = Button(window, text="About The Librarian", font=("Arial", 20), command= aboutRenderer.createWindow)

    #Set colors for elements
    l1['bg'] = '#898980'
    b1['bg'] = '#C5DAC1'
    b2['bg'] = '#C5DAC1'
    l2['bg'] = '#A9B2AC'
    b3['bg'] = '#C5DAC1'

    #Add elements to window
    l1.grid(column=0, row=0, padx=60)
    b1.grid(column=0, row=1, pady=15)
    b2.grid(column=0, row=2, pady=15)
    b3.grid(column=0, row=4, pady=15)

def loadSection(window, validText, validLabel, fileContents, fileDirectory):
    #Open file explorer to load section
    chosenFile = askopenfile(filetypes =[('Json Files', '*.json')])
    if (chosenFile == None):
        return

    #Check if chosen file is json
    if chosenFile.name.endswith('.json'):

        #Check if it is a correct json file
        try:
            fileContents.set(chosenFile.read())
            fileDirectory.set(chosenFile.name)
            toJson = json.loads(fileContents.get())
            print(toJson['isfilesortFile'])

            #Quit window and load in section viewer
            window.quit()
        except:
            validText.set("That file is not compatable.")
            validLabel.grid(column=0, row=3)
    else:
        validText.set("That file is not compatable.")
        validLabel.grid(column=0, row=3)

def sendData(fileContents, fileDirectory):
    #Create new window for section viewer
    sectionviewerRender.createWindow(fileContents.get(), fileDirectory.get())

createWindow()