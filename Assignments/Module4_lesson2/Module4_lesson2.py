# import the library
import sqlite3

# check that package is imported successfully
print("Successfully imported module")

# create or connect to a database
conn = sqlite3.connect("SGA_1_3.db")

# check that connection is successful
print("Database created successfully!")

# create a cursor object that allows the execution of SQL statements
cursor = conn.cursor()

# check that cursor is created successfully
# print("cursor created successfully \n", type(cursor))

# cursor.execute(""" CREATE TABLE students (
#                         first_name text,
#                         last_name text,
#                         age integer,
#                         email text,
#                         course text
#                         )
# """)

# check table created successfully
print("Table created successfully")

# created rows to input into the table
student_iist = [("Abubakar", "Adisa", 26, "adisaabubakar@gmail.com", "Data science"),
                ("Adebisi", "Afolabi", 28, "wasola.afolabi@yahoo.com", "Data science"),
                ("Adedoyin", "Abass", 25, "doyinabass0@gmail.com", "Data science"),
                ("Awonaike", "Tawakalitu", 27, "purpleduralumin@gmail.com", "Data science"),
                ("Babajide", "Adesugba", 23, "jide_ade@hotmail.com", "Data science"),
                ("Bukola", "Ajayi", 27,	"bukolam.ajayi@gmail.com", "Data science"),
                ("Binta", "Umar", 30, "ubinta63@yahoo.com", "Data science"),
                ("Christian", "Uzondu",	32, "uzonduchristian2@gmail.com", "Data science"),
                ("Cynthia", "Awiya", 34, "awiyac@yahoo.com", "Data science"),
                ("Deborah", "Olorunnishola", 29, "deboraholuwatobi247@gmail.com", "Data science"),
                ("Eke", "Ihuoma", 30, "ihuomaeke28@gmail.com", "Data science"),
                ("Esther", "Akpanowo", 35, "estherakpanowo@gmail.com", "Data science"),
                ("Eniola", "Osadare", 26, "dorcasosadare@gmail.com", "Data science"),
                ("Etariemi", "Louis", 31, "etariemilouis@gmail.com", "Data science"),
                ("Faith", "Amure", 30, "amuretalodabif@gmail.com", "Data science"),
                ("Ganiyat", "Shittu", 28, "ganiyatas@gmail.com", "Data science"),
                ("Gideon", "Uko", 32, "ukogideon13@gmail.com", "Data science"),
                ("Idowu", "Adesanya", 28, "idsworld22@yahoo.com", "Data science"),
                ("Joyce", "Ezeonwu", 32, "joyceokore@gmail.com", "Data science"),
                ("Kehinde", "Orolade", 25, "kehindeorolade@gmail.com", "Data science"),
                ("Kafayat", "Ibrahim", 36, "kafayatadenike10@gmail.com", "Data science"),
                ("Lawrence", "Aneshimokha", 38, "anelawrence1@gmail.com", "Data science"),
                ("Mariam", "Adeoti", 25, "adetutuadebola28@gmail.com", "Data science"),
                ("Ogechi", "Njemanze", 25,	"ogenjemz@gmail.com", "Data science"),
                ("Omowunmi", "Awonirana", 26, "mowunmi11@gmail.com", "Data science"),
                ("Placidus", "Ali", 39,	"Placidusali@gmail.com", "Data science"),
                ("Praise", "Emmanuel", 32, "praiseemmanuel9ic@gmail.com", "Data science"),
                ("Prince", "Ekeocha", 26, "prince.ekeocha@gmail.com", "Data science"),
                ("Rasheedat", "Sikiru", 28, "rasheedatsikiru@gmail.com", "Data science"),
                ("Ramotallah", "Jubril", 24, "jubrilramotallah03@gmail.com", "Data science"),
                ("Sheriiff", "Azeez", 29, "SheriffOlaitan71@gmail.com", "Data science"),
                ("Stephen", "Ogungbile", 27, "stephenfunso@gmail.com", "Data science"),
                ("Temitope", "Bamidele", 25, "bamideletemitope42@gmail.com", "Data science"),
                ("Theresa", "Karamor", 30, "teriekarie@gmail.com", "Data science"),
                ("Tina", "Uyateide", 35, "tinauyats@gmail.com", "Data science"),
                ("Victoria", "Chukwuno", 24, "chukwunovictoria@gmail.com", "Data science")


]

# Insert multiple rows into table
cursor.executemany("INSERT INTO students VALUES(?,?,?,?,?)", student_iist)

# confimation message for multiple rows
print("I have inserted", cursor.rowcount, "records into the table.")

# commit the database and table
conn.commit()

# close connection to the database
#conn.close()






































