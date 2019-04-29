import sqlite3
import sys
from easygui import *

def delete():
	delname=enterbox("Enter the name to be deleted")
	if delname is None:
	    msgbox("No contacts deleted")
	else:
		db = sqlite3.connect('contactdb')
		# Get a cursor object
		cursor = db.cursor()
		cursor.execute('''DELETE FROM users WHERE name=?''',(delname,))
		msgbox("Contact successfully deleted")
		db.commit()
		cursor.execute('''SELECT name, phone FROM users''')
		all_rows = cursor.fetchall()
		print ("Your contact list \n")
		#for row in all_rows:
		#	print('{} \t{}'.format(row[0], row[1]))
def search():
	db = sqlite3.connect('contactdb')
	# Get a cursor object
	cursor = db.cursor()
	name=enterbox("Enter the name")
	cursor.execute('''SELECT phone FROM users WHERE name=?''', (name,))
	user = cursor.fetchone()#fetch one row
	if user is None:
		msgbox("Not found")
	else:
		msgbox("The phone number is {}".format(user))

def create():
	def enbox():
		msg= "Enter your personal information"
		title = "Contact Application"
		fieldNames = ["Name","Phone"]#can be longer list
		users = []  # we start with blank list for the values
		users = multenterbox(msg,title, fieldNames)
		cursor.execute(''' INSERT INTO users(name, phone) VALUES(?,?)''',users)
		db.commit()
		print ("Reply was:", users)
	def Display():
	    cursor.execute('''SELECT name, phone FROM users''')
	    #user1 = cursor.fetchone() #retrieve the first row
	    #print(user1[0]) #Print the first column retrieved(user's name)
	    all_rows = cursor.fetchall()
	    print ("Your contact list \n")
		#for row in all_rows:
		#	print("hello")

	db = sqlite3.connect('contactdb')
	# Get a cursor object
	cursor = db.cursor()
	ynmsg=" Do you want to continue "
	title="Please confirm"
	while True:
		enbox()
		if not ynbox(ynmsg,title):
			break
	Display()
def update():
	   def Display():
		   cursor.execute('''SELECT name, phone FROM users''')
		   all_rows = cursor.fetchall()
		   print ("Your contact list \n")
		 #   for row in all_rows:
		#		print('{} \t {}'.format(row[0], row[1]))

		db = sqlite3.connect('contactdb')
		# Get a cursor object
		cursor = db.cursor()
		upname=enterbox("Enter the name")
		newno=1111
		cursor.execute(''' UPDATE users	SET phone=? WHERE name=? ''', (newno,upname,))
		db.commit()
		Display()
db = sqlite3.connect('contactdb')
# Get a cursor object
cursor = db.cursor()
cursor.execute('''  CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,phone TEXT)''')
db.commit()
msg = "Enter your choice"
choices = ["Add contact","Search","Delete","Update"]
reply = indexbox(msg,choices=choices)
print (reply)
if reply is 0:
	create()
if reply is 1:
	search()
if reply is 2:
	delete()
if reply is 3:
	update()
