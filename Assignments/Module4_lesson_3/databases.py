import sqlite3

print("successful")

# connet to a database
conn = sqlite3.connect("student.db")

# create a cursor object ( it helps us to execute our SQL command)
cursor = conn.cursor()

# Create Table
# cursor.execute(
#     """CREATE TABLE students_data(
#         first_name TEXT,
#         last_name TEXT,
#         email TEXT

#     )
#     """
# )

# check table created successfully
print("Table created successfully!")

# Insert many values into the table
# students_list =[("Will", "Johnson", "willjohnson@stutern.com"),
#                 ("John", "Smith", "johnsmith@stutern.com"),
#                 ("Katy", "Brown", "katybrown@stutern.com")]

# cursor.executemany("INSERT INTO students_data VALUES (?,?,?)", students_list)

# check values inserted successfully
# print("Values inserted successfully!")

# query the database
#cursor.execute("SELECT * FROM students_data")


# rows = cursor.fetchall()
# print("First Name" + "\t" + "Last Name" + "\t\t" + "Email")
# print("-" * 60)

# for row in rows:
#     print(row[0] +"\t\t" + row[1] + "\t\t" + row[2])

# Alter table
# cursor.execute("ALTER TABLE students_data RENAME TO students_details")

# check rename successful
print("Rename was successful")

# Adding a new column
#cursor.execute("ALTER TABLE students_details ADD COLUMN courses TEXT ;")

print("New column was added")

# Adding values to the new column
#cursor.execute("UPDATE students_details SET courses = 'Data science' ")

print("New values added to column")

cursor.execute("SELECT * FROM students_details")

# Fetching data from the updated table
rows = cursor.fetchall()
print("First Name" + "\t" + "Last Name" + "\t\t" + "Email" + "\t\t\t"+ "Courses")
print("-" * 80)

for row in rows:
    print(row[0] +"\t\t" + row[1] + "\t\t" + row[2] + "\t\t" + row[3])




# commit to database
conn.commit()
conn.close()

# Always remember to close your connection

