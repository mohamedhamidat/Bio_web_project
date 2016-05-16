import os 
import sqlite3

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(dir, 'db.sqlite3')

conn = sqlite3.connect(file_path)
c = conn.cursor()

def read_from_db():

	c.execute("SELECT * FROM 'webbioinformatics_contactus' ")
	for row in c.fetchall():
		# print row[4]
		print row


c.execute("select name from sqlite_master where type='table'")
print(c.fetchall())

read_from_db()



