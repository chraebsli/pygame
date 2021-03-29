import mysql.connector
from mysql.connector import errorcode

def start():
	# Obtain connection string information from the portal
	config = {
	'host':'188.154.233.211:3306', # remote
	#'host':'192.168.60.146', # local
	'user':'coinchaser',
	'password':'Coinchaser2021',
	'database':'coinchaser'
	}

	'''
	# Construct connection string
	try:
		conn = mysql.connector.connect(**config)
		print("Connection established")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with the user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cursor = conn.cursor()
	'''

	conn = mysql.connector.connect(**config)
	cursor = conn.cursor()
	# Insert some data into table
	cursor.execute("INSERT INTO leaderboard (crdate, playername, points, playedTime) VALUES (%s,%s,%s,%s)", ("16.03.", "test3", 400, "1:45.65"))

	# Cleanup
	conn.commit()
	cursor.close()
	conn.close()
	print("Done.")

	#INSERT INTO scores (crdate, playername, points, playtime) VALUES (%s,%s,%s,%s)", ("16.03.", "test1", 400, "1:45.65")

start()