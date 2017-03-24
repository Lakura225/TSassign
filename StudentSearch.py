import sqlite3 as db
from tkinter import *

#Formatting
TITLE_FONT = ("Helvetica", 18 )
FONT=("Helvetica", 13)

class App:


    def __init__(self, master):

        root.title("Personal Tutor System") #Define root title

        #Declare all variables for initialisation
        self.master = master
        self.search=StringVar()
        self.search2=StringVar()
        self.frame = Frame(master)
        self.connection = db.connect('Students.db')
        self.cur = self.connection.cursor()
        self.StrtSrch = Button(self.frame, text = 'Search',font=FONT, command = self.RtrnResults)
        self.entry1=Entry(root, textvariable=self.search)
        self.entry2 = Entry(root, textvariable=self.search2)

        #Decalare labels for GUI
        Label(root,text="Cardiff university Personal tutor system",font=TITLE_FONT).grid(row=1,sticky=W, columnspan=2)
        Label(root,text="Please use either field for your search.").grid(row=2, columnspan=2, sticky=W)
        Label(root,text="Please enter a students Surname:").grid(row=3, sticky=W)
        Label(root,text="Please enter a students Number in lower case:").grid(row=4, sticky=W)

        #Deploy interactive parts to GUI
        self.StrtSrch.grid(row = 3,column=2, columnspan=2)
        self.entry1.grid(row = 3, column=2)
        self.entry2.grid(row = 5, column=2)
        self.frame.grid()

    def RtrnResults(self):

        #retrieve inputs
        searchent1 = self.search.get()
        searchent2 = self.search2.get()

        #retrieve data
        data = self.ReadDB(searchent1,searchent2)
        row = 8

        #declare faux table labels
        Label(self.master, text='Student Code').grid(row=7, column=0)
        Label(self.master, text='Surname').grid(row=7, column=1)
        Label(self.master, text='Forename1').grid(row=7, column=2)
        Label(self.master, text='Forename2').grid(row=7, column=3)
        Label(self.master, text='Tutor').grid(row=7, column=4)
        Label(self.master, text='Course').grid(row=7, column=5)
        Label(self.master, text='Year').grid(row=7, column=6)
        Label(self.master, text='Email').grid(row=7, column=7)

        #process data and display in faux table
        for index, dat in enumerate(data):

            Label(self.master, text=dat[0]).grid(row=row+index+1, column=0)
            Label(self.master, text=dat[1]).grid(row=row+index+1, column=1)
            Label(self.master, text=dat[2]).grid(row=row+index+1, column=2)
            Label(self.master, text=dat[3]).grid(row=row+index+1, column=3)
            Label(self.master, text=dat[4]).grid(row=row+index+1, column=4)
            Label(self.master, text=dat[5]).grid(row=row+index+1, column=5)
            Label(self.master, text=dat[6]).grid(row=row+index+1, column=6)
            Label(self.master, text=dat[7]).grid(row=row+index+1, column=7)

    def ReadDB(self, searchent1,searchent2):

        #fetch data from the DB
        self.cur.execute("SELECT * FROM Student_List WHERE Surname = ? OR Student_Code = ?",(searchent1, searchent2,))
        return self.cur.fetchall()

#launch
root = Tk()
app = App(root)
root.mainloop()