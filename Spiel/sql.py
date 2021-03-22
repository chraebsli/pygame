import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'188.154.233.211',
  'user':'coinchaser',
  'password':'Coinchaser2021',
  'database':'coinchaser',
  #'client_flags': [ClientFlag.SSL],
  #'ssl_cert': '/var/wwww/html/DigiCertGlobalRootG2.crt.pem'
}

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

  # Insert some data into table
  cursor.execute("INSERT INTO leaderboard (crdate, playername, points, playedTime) VALUES (%s,%s,%s,%s)", ("16.03.", "test1", 400, "1:45.65"))

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")

  #INSERT INTO scores (crdate, playername, points, playtime) VALUES (%s,%s,%s,%s)", ("16.03.", "test1", 400, "1:45.65")