#Code could be bollocks, just following the api, cant test it atm
import sqlite3
from tkinter import *
from tkinter.ttk import *
Search = "testor"
conn = sqlite3.connect('Students.db')

class App(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.connection = sqlite3.connect('Students.db')
        self.cur = self.connection.cursor()
        #self.CreateUI()
        self.DisplayThem()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('Student_Code', 'Surname', 'Forename1', 'Forename2', 'Tutor', 'Acad_Year', 'Univ_Email')
        tv.heading("#0", text='Student Code', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('Surname', text='Surname')
        tv.column('Surname', anchor='center', width=100)
        tv.heading('Forename1', text='Forename1')
        tv.column('Forename1', anchor='center', width=100)
        tv.heading('Forename2', text='Forename2')
        tv.column('Forename2', anchor='center', width=100)
        tv.heading('Tutor', text='Tutor')
        tv.column('Tutor', anchor='center', width=100)
        tv.heading('Acad_Year', text='Year')
        tv.column('Acad_Year', anchor='center', width=100)
        tv.heading('Univ_Email', text='Email')
        tv.column('Univ_Email', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
    def DisplayThem(self):
        data = self.ReadDB()
        Label(self.master, text='Student Code').grid(row=0, column=0)
        Label(self.master, text='Surname').grid(row=0, column=1)
        Label(self.master, text='Forename1').grid(row=0, column=2)
        Label(self.master, text='Forename2').grid(row=0, column=3)
        Label(self.master, text='Tutor').grid(row=0, column=4)
        Label(self.master, text='Year').grid(row=0, column=5)
        Label(self.master, text='Tutor Code').grid(row=0, column=6)
        Label(self.master, text='Email').grid(row=0, column=7)
        for index, dat in enumerate(data):
            Label(self.master, text=dat[0]).grid(row=index+1, column=0)
            Label(self.master, text=dat[1]).grid(row=index+1, column=1)
            Label(self.master, text=dat[2]).grid(row=index+1, column=2)
            Label(self.master, text=dat[3]).grid(row=index+1, column=3)
            Label(self.master, text=dat[4]).grid(row=index+1, column=4)
            Label(self.master, text=dat[5]).grid(row=index+1, column=5)
            Label(self.master, text=dat[6]).grid(row=index+1, column=6)
            Label(self.master, text=dat[7]).grid(row=index+1, column=7)

    def ReadDB(self):
        self.cur.execute("SELECT * FROM Student_List WHERE Tutor = ?",(Search,))
        return self.cur.fetchall()

def main():
    root = Tk()
    root.title("List of Students")
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

#Take the what is in the search bar and name it search
def displaytutees(search):
	c = conn.cursor()

	#Attempting to retreive data from sqlite
	for row in c.execute('SELECT * FROM Student list ORDER BY Student ID'):
		#Put the result in the UI, however we are doing that
		print (row)