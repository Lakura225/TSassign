import sqlite3 as db


conn = db.connect("students.db")

def UsrInput(searchtype,query):

	Query1 = normalise_input(query) #eliminate most problems with user input

	#check which field user is searching by for personal tutor.

	if searchtype == 0:
		blah
	elif searchtype == 1:
		blarh
	elif searchtype == 2:
		barl
	elif searchtype ==3:
		lashdh
	else:
		return False

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