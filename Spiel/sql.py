import sqlite3,json
path = 'c:/Users/Local-Admin/Documents/_git/github/pygame/Spiel/resources/'

db = sqlite3.connect(path+"dataa.db") 
print(db)
cursor = db.cursor()

with open(path+'web/scores.json') as file:
    data = json.load(file)

command = f"""INSERT INTO SCORES VALUES (1, 'Time', 'name', 3); """
cursor.execute(command) 

db.commit() 
db.close() 
"""
index=1
for p in data['scores']:
    time = p['time']
    name = p['name']
    points = p['points']
    command = f"INSERT INTO SCORES VALUES (1, 'Time', 'name', 3);"
    index+=1
    cursor.execute(command) 
"""