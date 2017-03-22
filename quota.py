from tkinter import *
from tkinter import ttk
import sqlite3
import csv

TITLE_FONT = ("Helvetica", 18 )
FONT=("Helvetica", 13)
root=Tk()


inp=StringVar()

root.title("Personal Tutor System")

def getvalue():
    conn=sqlite3.connect('students.db')
    cursor = conn.cursor()


    cursor.execute ("SELECT StudentsAssigned FROM Tutors WHERE Tutor_ID= ?",(inp.get(),))
    
    if( len(inp.get()) == 0):
        next
    else:
        rows = cursor.fetchall()
        
        for row in rows:
            Label(root, text=" The quota of tutees Tutor " + inp.get()+" has is: " ,font=FONT).grid(row=10,column=0,sticky=W, columnspan=3)
            Label(root, text=rows , font=FONT).grid(row=10,column=1,sticky=W, columnspan=2)
    
Label(root,text="Quota of the tutees",font=TITLE_FONT).grid(row=0, column=1,sticky=W)
Label(root, text="The sytem will only return data for valid ID's so if no output is returned please re enter the ID ",font=FONT).grid(row=2, column=0, columnspan=2)
Label(root,text="Please enter a tutor ID: ", font=FONT).grid(row=3, column=0, sticky=W)
Entry(root, width=50, textvariable= inp).grid(row=3, column=1, sticky=W)
Button(root, text="Enter", command=getvalue).grid(row=3, column=2, sticky=W)


root.mainloop()

