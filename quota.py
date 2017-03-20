import sqlite3
import csv

conn=sqlite3.connect('Tutor.db')
cursor = conn.cursor()

in_id = input('Enter the tutors ID: ')

while (in_id ==""):
    in_id = input('Enter the tutors ID: ')
else: next 
  
print('No of tutees', in_id ,'has is :' )

cursor.execute ("SELECT students assigned FROM Tutor WHERE ID= ?",(in_id))

rows = conn.fetchall()

for row in rows:
    print(row)


