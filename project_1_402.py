import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="---",
    database="menagerie"
)

cursor = conn.cursor()

cursor.execute("SELECT name, birth, MONTH(birth) as birth_month FROM pet")

records = cursor.fetchall()
for record in records:
    print(record)

cursor.close()
conn.close()