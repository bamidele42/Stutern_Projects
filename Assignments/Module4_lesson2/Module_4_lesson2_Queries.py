import sqlite3
from Module4_lesson2 import conn
from Module4_lesson2 import cursor
cursor.execute("SELECT * FROM students")

rows = cursor.fetchmany(10)
print("First Name" + "\t\tLast Name" + "\t\tAge" + "\t\tEmail" + "\t\tCourse")
print("-" *100)

for row in rows:
    print(row[0] + " \t\t " + row[1] + " \t\t " + str(row[2]) +" \t\t " + row[3] + " \t\t " + row[4])

conn.commit
conn.close()