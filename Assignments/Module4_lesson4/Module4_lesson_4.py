
import sqlite3

# print connect to database
conn = sqlite3.Connection("celeb.db")

# Check connection
print("successfully connected to database")

# create a cursor object
cursor = conn.cursor()

print("cursor object created successfully")

# Create celeb table
# cursor.execute("""
# CREATE TABLE celebrities(
#         name text,
#         genre text,
#         num_albums integer,
#         age integer,
#         awards integer,
#         years_in_industry integer)
# """)

# check table created successfully
#print("Table created successfully!")

# list of celebrity names
# list = [("BurnaBoy", "Afro", 5, 30, 10, 15), ("Wizkid", "Afro Hiphop", 6, 28, 19, 20), 
#         ("Davido", "Afro Hiphop", 4, 27, 8, 12), ("Mi", "Rap", 5, 33, 11, 22),
#         ("Olamide", "Rap", 8, 34, 13, 18), ("Phyno", "Rap", 6, 37, 9, 15), 
#         ("Falz", "Rap", 4, 27, 6, 12), ("WandeCoal", "R&B", 5, 33, 8, 19),
#         ("Dbanj", "Afro Hiphop", 8, 40, 12, 22), ("DonJazzy", "Afro Hiphop", 1, 45, 3, 20),
#         ("TimiDakolo", "R&B", 6, 42, 15, 22), ("Flavour", "HighLife", 7, 39, 7, 20),
#         ("Psquare", "DanceHall", 10, 42, 15, 22), ("AdekunleGold", "Afro HipHop", 5, 39, 5, 10),
#         ("Simi", "R&B", 3, 28, 3, 10), ("KissDaniel", "DanceHall", 4, 33, 5, 12),
#         ("Tekno", "Afro HipHop", 3, 30, 3, 14), ("Brymo", "R&B", 7, 38, 6, 22),
#         ("2Baba", "Afro Hiphop", 10, 45, 15, 25)]
        
# cursor.executemany("INSERT INTO celebrities VALUES (?, ?, ?, ?, ?, ?)", list)

# check that values are inserted successfully
#print("successfully inserted values")

# select items from the table
#cursor.execute("SELECT * FROM celebrities")

# Query the table
query = """
SELECT name AS "Artiste_Name"
FROM celebrities
"""
cursor.execute(query)

rows = cursor.fetchmany(5)
# print("Name" + "\t" +"Genre" + "\t" + "Num_album" +"\t" + "Age"+ "\t"+ "Award"+ "\t" + "Years_in_industry")
# print("-" *60 )
for row in rows:
    print(row)

#     print(row[0] + "\t" + row[1]+ "\t" +str(row[2]) + "\t" +str(row[3]) + "\t" +str(row[4]) + "\t" +str(row[5])) 

# commit changes
conn.commit()
conn.close()