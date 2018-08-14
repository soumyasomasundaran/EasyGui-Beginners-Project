import sqlite3
import sys
from easygui import *
#DATABASE CONNECTION
db = sqlite3.connect('test1')
# Get a cursor object
cursor = db.cursor()
#cursor.execute('''    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,phone TEXT)''')

def enbox():
	msg= "Enter your personal information"
	title = "Contact Application"
	fieldNames = ["Name","Phone"]
	users = []  # we start with blanks for the values
	users = multenterbox(msg,title, fieldNames)
	cursor.execute(''' INSERT INTO users(name, phone) VALUES(?,?)''',users)
	db.commit()
	print ("Reply was:", users)

def display():
	cursor.execute('''SELECT name, phone FROM users''')
	user1 = cursor.fetchone() #retrieve the first row
	#print(user1[0]) #Print the first column retrieved(user's name)
	all_rows = cursor.fetchall()
	for row in all_rows:
 		# row[0] returns the first column in the query (name), row[1] returns email column.
		print('{} {}'.format(row[0], row[1]))

def search():
	name=enterbox("Enter the name")
	cursor.execute('''SELECT phone FROM users WHERE name=?''', (name,))
	user = cursor.fetchone()
	msgbox("The phone number is {}".format(user))

def delete(delname):
	delete_username = delname
	cursor.execute('''DELETE FROM users WHERE name = ? ''', (delete_username,))
	db.commit()
	

choice=["Insert","Search","Delete","Display"]
reply=buttonbox("Enter your choice",choices=choice)
if reply==choice[0]:
	while True:
		enbox()
		if not ynbox(" Do you want to continue ","Please confirm"):
			 break

elif reply==choice[1]:
	search()
elif reply==choice[2]:
	delname=enterbox("Enter the name")
	delete(delname)
elif reply==choice[3]:
	display()

	




