#Code could be bollocks, just following the api, cant test it atm
import sqlite3
from tkinter import *
from tkinter.ttk import *
conn = sqlite3.connect('name.db')

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('student_id', 'student_name', 'course')
        tv.heading("#0", text='Tutor', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('student_id', text='Studen ID')
        tv.column('student_id', anchor='center', width=100)
        tv.heading('student_name', text='Student name')
        tv.column('student_name', anchor='center', width=100)
        tv.heading('course', text='Course')
        tv.column('course', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.cur.execute("SELECT * FROM Student List")
        return self.cur.fetchall()

def main():
    root = Tk()
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