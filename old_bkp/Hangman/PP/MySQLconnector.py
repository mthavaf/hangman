import mysql.connector

conn = mysql.connector.connection(user='',password='',host='',database='')

cur = conn.cursor()

cur.execute('')

for data.....datan in cur:
	print

cur.close()

conn.close()
