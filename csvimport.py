# https://www.google.co.uk/webhp?sourceid=chrome-instant&rlz=1C1PRFI_enGB711GB711&ion=1&espv=2&ie=UTF-8#q=insert+into+mysql+from+array+python&*
# row 1 student id
# row 2 name
# row 3 surname
# row 4 course
# row 5 email
"""
def CSVtoMySql():
    conn = sqlite3.connect('students.db')
    q = INSERT IGNORE into students (
            sID, sName, sSurname, sSurname2, sTutor, sCourse, sAcadYear, sEmail )
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s)

    try:
        conn.executemany(q, 'students.db')
        conn.commit()
    except:
        conn.rollback()

"""
import csv
import sqlite3

Student_Code = []
Surname = []
Forname1 = []
Forname2 = []
Tutor = []
Course = []
Acad_Year = []
Univ_Email = []
s=[Student_Code, Surname, Forname1, Forname2, Tutor, Course, Acad_Year, Univ_Email]

def openCSV():
    with open("test.csv") as csvfile:
        rdr = csv.reader(csvfile)
        next(rdr)
        for row in rdr:
            Student_Code.append((str(row[0])))
            Surname.append((str(row[1])))
            Forname1.append((str(row[2])))
            Forname2.append((str(row[3])))
            Tutor.append((str(row[4])))
            Course.append((str(row[5])))
            Acad_Year.append((str(row[6])))
            Univ_Email.append((str(row[7])))

        return Student_Code, Surname, Forname1, Forname2, Tutor, Course, Acad_Year, Univ_Email

def CSVtoMySql():
    conn = sqlite3.connect('students.db')
    q = "INSERT INTO Student VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s)", s

    try:
        conn.executemany(q, s)
        conn.commit()
    except:
        conn.rollback()




def method2(Filename):
    import csv, sqlite3

    con = sqlite3.connect('students.db')
    cur = con.cursor()
    #cur.execute("CREATE TABLE Student (Student_Code, Surname, Forname1, Forname2, Tutor, Course, Acad_Year, Univ_Email);")  # use your column names here (we already have a database)

    with open(Filename, 'r') as fin:  # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i['Student_Code'], i['Surname'], i['Forename1'], i['Forename2'], i['Tutor'], i['Course'], i['Acad_Year'], i['Univ_Email'],) for i in dr]
# VALUES(?,?,?,?)''',(name1,phone1, email1, password1))
    cur.executemany(
        "INSERT INTO Student_List (Student_Code, Surname, Forename1, Forename2, Tutor, Course, Acad_Year, Univ_Email) VALUES (?,?,?,?,?,?,?,?),(Student_Code, Surname, Forename1, Forename2, Tutor, Course, Acad_Year, Univ_Email);",
        to_db)
    con.commit()
    con.close()
    
