import sqlite3

# print connect to database
conn = sqlite3.Connection("celeb.db")

# Check connection
print("successfully connected to database")

# create a cursor object
cursor = conn.cursor()

print("cursor object created successfully")

# Query the table
# Who is the oldest celebrity?
def oldest_celebrity(column):
    query = """
    SELECT name, Genre, MAX(age), num_albums
    FROM celebrities
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    print("Name" + "\t" +"Genre" + "\t" + "Age"+ "\t" + "num_album")
    print("-" *60 )
    for row in rows:
        print(f"{row[0]} {row[1]} \t {row[2]} \t {row[3]}")

#oldest_celebrity("age")

# Which celebrity has been in the industry the longest?
def longest_celebrity(column):
    query = """
    SELECT name, Genre, MAX(years_in_industry), num_albums
    FROM celebrities
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    print("Name" + "\t" +"Genre" + "\t" + "Years_in_industry" + "\t" + "Num_album")
    print("-" *60 )
    for row in rows:
        print(f"{row[0]} \t {row[1]} \t {row[2]} \t\t {row[3]}")

#longest_celebrity("years_in_industry")

# Which celebrity has the least number of albums?
def least_album(column):
    query = """
    SELECT name, Genre, MIN(num_albums), age, years_in_industry
    FROM celebrities
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    print("Name" + "\t" +"Genre" + "\t" + "Num_album" + "\t" + "age" + "\t" + "years_in_industry" )
    print("-" *60 )
    for row in rows:
        print(f"{row[0]} {row[1]} {row[2]} \t\t{row[3]} \t {row[4]}")

#least_album("num_albums")

# What is the most popular genre of music amongst all celebrities in the dataset?
def popular_music(column):
    query = """
    SELECT MAX(genre)
    FROM celebrities
    """
    cursor.execute(query)

    rows = cursor.fetchall()
 
    for row in rows:
        print("".join(row))

popular_music("genre")


# print(row[0] + "\t" + row[1]+ "\t" +str(row[2]) + "\t" +str(row[3]) + "\t" +str(row[4]) + "\t" +str(row[5])) 

# commit changes
conn.commit()
conn.close()