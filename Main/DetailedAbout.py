from tkinter import *
from tkinter import ttk

def createWindow():
    #Create window object
    window = Tk()
    window.attributes('-topmost', True)

    #Specify window constraints
    window.config(width="800", height="600", bg="#A9B2AC")
    window.title("The Librarian")
    addwindowElements(window)
    
    #Launch window
    window.mainloop()

def addwindowElements(window):
    #Description text
    fileText = "The Librarian uses a JSON file to store all chosen file directories within your personal sections. This allows users to manually add directories if desired in the JSON file but also prevents possible dangerous system interactions."
    saveText = "How exacty does The Librarian save space? The Librarian saves space by allowing users to point to specific files paths without having to move or copy the specified file. This will in turn save an immense amount of storage by only storing small strings of data."
    undoredoText = "The Librarian uses previous file states to implement an Undo and Redo functionality. By storing passed JSON files, the user can easily revert to an older or newer version of the file. This functionality has relatively no limit allowing a large amount of freedom to the user and helps prevent mistakes."
    dangersText = "The Librarian checks each file that it is first a JSON file and then for the correct syntax before opening the file. This prevents the software from manipulating any files that have not been created for the software. Users can breath easy knowing only correct files can be opened."
        
    #Create window elements
    l1 = Label(window, text="How does the Librarian work?", font=("Arial", 45))

    l2 = Label(window, text="File Usage:", font=("Arial", 30))
    t1 = Label(window, text=fileText, font=("Arial", 16), wraplength=750)

    l3 = Label(window, text="Saving Space:", font=("Arial", 30))
    t2 = Label(window, text=saveText, font=("Arial", 16), wraplength=750)

    l4 = Label(window, text="Undo/Redo:", font=("Arial", 30))
    t3 = Label(window, text=undoredoText, font=("Arial", 16), wraplength=750)

    l5 = Label(window, text="Possible Dangers:", font=("Arial", 30))
    t4 = Label(window, text=dangersText, font=("Arial", 16), wraplength=750)

    #Set colors for elements
    l1['bg'] = '#898980'
    l2['bg'] = '#A9B2AC'
    t1['bg'] = '#A9B2AC'
    l3['bg'] = '#A9B2AC'
    t2['bg'] = '#A9B2AC'
    l4['bg'] = '#A9B2AC'
    t3['bg'] = '#A9B2AC'
    l5['bg'] = '#A9B2AC'
    t4['bg'] = '#A9B2AC'


    #Add elements to window
    l1.grid(column=0, row=0, padx=60, pady=15)
    l2.grid(column=0, row=1, padx=60, pady=15)
    t1.grid(column=0, row=2, padx=60, pady=0)
    l3.grid(column=0, row=3, padx=60, pady=15)
    t2.grid(column=0, row=4, padx=60, pady=0)
    l4.grid(column=0, row=5, padx=60, pady=15)
    t3.grid(column=0, row=6, padx=60, pady=0)
    l5.grid(column=0, row=7, padx=60, pady=15)
    t4.grid(column=0, row=8, padx=60, pady=0)