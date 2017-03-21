# https://www.google.co.uk/webhp?sourceid=chrome-instant&rlz=1C1PRFI_enGB711GB711&ion=1&espv=2&ie=UTF-8#q=insert+into+mysql+from+array+python&*
# row 1 student id
# row 2 student name(whole)
# row 3 course
# row 4 email
# row 5 wifi password lelele
import csv
import sqlite3

sID = []
sName = []
sSurn = []
sEmail = []
sCourse = []

def openCSV(filename):
    with open(filename) as csvfile:
        rdr = csv.reader(csvfile)
        next(rdr)
        for row in rdr:
            sID.append((int(row[0])))
            sName.append((str(row[1])))
            sSurn.append((str(row[2])))
            sEmail.append((str(row[3])))
            sCourse.append((str(row[4])))
            sID.sort()
            sName.sort()
            sEmail.sort()
            sCourse.sort()
            
        return sID, sName, sSurn, sEmail, sCourse
#openCSV("test.csv")

def CSVtoMySql():
    conn = sqlite3.connect('students.db')
    q = """ insert ignore into TABLE1 (
            sID, sName, sEmail, sCourse )
            values (%s,%s,%s,%s)
        """
    try:
        conn.executemany(q, 'students.db')
        conn.commit()
    except:
        conn.rollback()

