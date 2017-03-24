import sqlite3
from tkinter import *
import os
conn = sqlite3.connect('Students.db')

TITLE_FONT = ("Helvetica", 18 )
FONT=("Helvetica", 13)

class App:
    def __init__(self, master):
        self.master = master
        root.title("Personal Tutor System")
        self.connection = sqlite3.connect('Students.db')
        self.cur = self.connection.cursor()
        Label(root,text="Cardiff university Personal tutor system",font=TITLE_FONT).grid(row=2,sticky=W, columnspan=2)
        self.frame = Frame(master)
        self.search=StringVar()
        Label(root,text="Enter a tutor name here:").grid(row=3, sticky=W)
        self.a = Button(self.frame, text = 'Enter',font=FONT, command = self.DisplayThem)
        self.b=Entry(root, textvariable=self.search)
        self.a.grid(row = 3,column=2, columnspan=2)
        self.b.grid(row = 4, column=2)
        self.frame.grid()

    def DisplayThem(self):
        searched = 'testory'
        searched = self.search.get()
        data = self.ReadDB(searched)
        Label(self.master, text='Student Code').grid(row=7, column=0)
        Label(self.master, text='Surname').grid(row=7, column=1)
        Label(self.master, text='Forename1').grid(row=7, column=2)
        Label(self.master, text='Forename2').grid(row=7, column=3)
        Label(self.master, text='Tutor').grid(row=7, column=4)
        Label(self.master, text='Course').grid(row=7, column=5)
        Label(self.master, text='Year').grid(row=7, column=6)
        Label(self.master, text='Email').grid(row=7, column=7)
        row = 8
        for index, dat in enumerate(data):
            Label(self.master, text=dat[0]).grid(row=row+index+1, column=0)
            Label(self.master, text=dat[1]).grid(row=row+index+1, column=1)
            Label(self.master, text=dat[2]).grid(row=row+index+1, column=2)
            Label(self.master, text=dat[3]).grid(row=row+index+1, column=3)
            Label(self.master, text=dat[4]).grid(row=row+index+1, column=4)
            Label(self.master, text=dat[5]).grid(row=row+index+1, column=5)
            Label(self.master, text=dat[6]).grid(row=row+index+1, column=6)
            Label(self.master, text=dat[7]).grid(row=row+index+1, column=7)

    def ReadDB(self, searched):
        self.cur.execute("SELECT * FROM Student_List WHERE Tutor = ?",(searched,))
        return self.cur.fetchall()


root = Tk()
app = App(root)
root.mainloop()
