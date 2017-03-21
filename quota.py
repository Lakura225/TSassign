import sqlite3
import csv


conn=sqlite3.connect('students.db')
cursor = conn.cursor()

in_id = input('Enter the tutors ID: ')

while (in_id ==""):
    in_id = input('Enter the tutors ID: ')

  
print('No of tutees', in_id ,'has is :' )

cursor.execute ("SELECT StudentsAssigned FROM Tutors WHERE Tutor_ID= ?",(in_id))

rows = cursor.fetchall()

for row in rows:
    print(row)


