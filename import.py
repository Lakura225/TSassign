# https://www.google.co.uk/webhp?sourceid=chrome-instant&rlz=1C1PRFI_enGB711GB711&ion=1&espv=2&ie=UTF-8#q=insert+into+mysql+from+array+python&*
# row 1 student id
# row 2 name
# row 3 surname
# row 4 course
# row 5 email
import csv
import sqlite3

sID = []
sName = []
sSurname = []
sSurname2 = []
sTutor = []
sCourse = []
sAcadYear = []
sEmail = []


def openCSV(filename):
    with open(filename) as csvfile:
        rdr = csv.reader(csvfile)
        next(rdr)
        for row in rdr:
            sID.append((int(row[0])))
            sName.append((str(row[1])))
            sSurname.append((str(row[2])))
            sSurname2.append((str(row[3])))
            sTutor.append((str(row[4])))
            sCourse.append((str(row[5])))
            sAcadYear.append((str(row[6])))
            sEmail.append((str(row[7])))

        return sID, sName, sSurname, sSurname2, sTutor, sCourse, sAcadYear, sEmail


def CSVtoMySql():
    conn = sqlite3.connect('students.db')
    q = """ INSERT IGNORE into students (
            sID, sName, sSurname, sSurname2, sTutor, sCourse, sAcadYear, sEmail )
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    try:
        conn.executemany(q, 'students.db')
        conn.commit()
    except:
        conn.rollback()


def method2():
    import csv, sqlite3

    con = sqlite3.connect('students.db')
    cur = con.cursor()
    # cur.execute("CREATE TABLE t (col1, col2);")  # use your column names here (we already have a database)

    with open('test.csv', 'rb') as fin:  # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i['Student ID'], i['Name(s)'], i['Surname'], i['Course'], i['Tutor'],) for i in dr]

    cur.executemany(
        "INSERT INTO students (Student_Code, Surname, Forname1, Forname2, Tutor, Course, Acad_Year, Univ_Email) VALUES (sID, sName, sSurname, sSurname2, sTutor, sCourse, sAcadYear, sEmail);",
        to_db)
    con.commit()
    con.close()
    return
