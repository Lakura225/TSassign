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
sEmail = []
sCourse = []
sSurname = []

def openCSV(filename):
    with open(filename) as csvfile:
        rdr = csv.reader(csvfile)
        next(rdr)
        for row in rdr:
            sID.append((int(row[0])))
            sName.append((str(row[1])))
            sSurname.append((str(row[2])))
            sEmail.append((str(row[3])))
            sCourse.append((str(row[4])))
            sID.sort()
            sName.sort()
            sSurname.sort()
            sEmail.sort()
            sCourse.sort()

        return sID, sSurname, sName, sEmail, sCourse


def CSVtoMySql():
    conn = sqlite3.connect('students.db')
    q = """ INSERT IGNORE into TABLE1 (
            sID, sSurname, sName, sEmail, sCourse )
            values (%s, %s, %s, %s, %s)
        """
    try:
        conn.executemany(q, 'students.db')
        conn.commit()
    except:
        conn.rollback()


def MySqlsort():

    return
