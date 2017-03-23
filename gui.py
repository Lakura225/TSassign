
from tkinter import *
import os

TITLE_FONT = ("Helvetica", 18 )
FONT=("Helvetica", 13)

class App:
    def __init__(self, master):
        root.title("Personal Tutor System")
        Label(root,text="Cardiff university Personal tutor system",font=TITLE_FONT).grid(row=2,sticky=W, columnspan=2)
        self.frame = Frame(master)
        self.a = Button(self.frame, text = 'Quota of tutees ', font=FONT, command = self.openFile1)
        self.b = Button(self.frame, text = 'Search for individual students ',font=FONT, command = self.openFile2)
        self.c = Button(self.frame, text = 'list of tutees for a particular personal tutor ',font=FONT, command = self.openFile3)
        self.a.grid(row = 3,column=2, columnspan=2)
        self.b.grid(row = 4,column=2  )
        self.c.grid(row = 5,column=2 )
        self.frame.grid()
    def openFile1(self):
        os.startfile("tuteequota.py")
    
    def openFile2(self):
        os.startfile("tuteequota.py")#place your file name here in accordance to the button names above

    def openFile3(self):
        os.startfile("displaytutees.py")

root = Tk()
app = App(root)
root.mainloop()
