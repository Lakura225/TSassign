import sqlite3 as db


conn = db.connect("students.db")

def TutorSearch(Surname,name,Title):

	with conn:
		conn.row_factory = db.Row

		cur = conn.cursor()
		cur.execute("SELECT Tutor_ID FROM Tutors WHERE Name = name AND Surname = surname" )
		Tutornum = cur.fetchall()
		return Tutornum

def StudentList(tutornumber):


def remove_punct(text):

    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct

def remove_spaces(text):

    text = text.strip(" ")
    ' '.join(text.split())
    return text


def normalise_input(user_input):

    no_punct = remove_punct(user_input).lower()
    no_spaces = remove_spaces(no_punct)
    words = no_spaces.split()

    return filtered