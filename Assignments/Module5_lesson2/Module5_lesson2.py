# import dependencies
import sqlite3
import csv

# create  waec database
conn = sqlite3.connect("waec.db")

# create a cursor
cursor = conn.cursor()

# create a waec_scores table
# table = """CREATE TABLE waec_scores (
#                     name text,
#                     physics integer,
#                     chemistry integer,
#                     mathematics integer,
#                     economics integer,
#                     accounting integer,
#                     english integer,
#                     literature integer,
#                     agriculture integer,
#                     geography integer
#                 )"""

# cursor.execute(table)
# print("table created successfully!!")

# open the csv file and read it using the csv module
# with open("waec_1.csv", "r") as data:
#     waec_file = csv.reader(data)
#     next(waec_file)
#     cursor.executemany("""INSERT INTO waec_scores VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", waec_file)

# print("read successfully!!")

query = cursor.execute("SELECT * FROM waec_scores")
rows = cursor.fetchall()
print(f"Name\t\tphysics chemistry mathematics economics accounting english literature agriculture geography")
for row in rows:
    name, physics, chemistry, mathematics, economics, accounting, english, literature, agriculture, geography = row
    print(f"{name:10}\t{physics}\t{chemistry}\t{mathematics:10}\t{economics:5}\t{accounting:5}\t{english:5}\t{literature:5}\t{agriculture:10}\t{geography:10}")







# commit changes and close connection
conn.commit()
conn.close()