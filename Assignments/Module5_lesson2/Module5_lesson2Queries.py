# import dependencies
import sqlite3
import csv

# create  waec database
conn = sqlite3.connect("waec.db")

# create a cursor
cursor = conn.cursor()

# select all items
# cursor.execute("SELECT * FROM waec_scores")

# Which student scored the highest in maths
def highest_in_math():
        query_1 = """SELECT name, MAX(mathematics)
            FROM waec_scores;
                """
        cursor.execute(query_1)

        rows = cursor.fetchall()
        for row in rows:
            print(f"The best student in mathematics is {row[0]} with {row[1]} scores")

highest_in_math()

# Which student scored the lowest in english
def lowest_in_english():
        query_2 = """SELECT name, MIN(english)
            FROM waec_scores;
                """
        cursor.execute(query_2)

        rows = cursor.fetchall()
        for row in rows:
            print(f"The student the lowest score in english is {row[0]} with {row[1]} scores")

lowest_in_english()

# What is the average score of students in maths

def AVG_score_in_math():
        query_3 = """SELECT ROUND(AVG(mathematics),0)
            FROM waec_scores;
                """
        cursor.execute(query_3)

        rows = cursor.fetchall()
        for row in rows:
            print(f"The average score of students in mathematics is {row[0]}")

AVG_score_in_math()


# What is the average score of students in english
def AVG_score_in_english():
        query_3 = """SELECT ROUND(AVG(english),0)
            FROM waec_scores;
                """
        cursor.execute(query_3)

        rows = cursor.fetchall()
        for row in rows:
            print(f"The average score of students in English is {row[0]}")

AVG_score_in_english()

# Who is the best performing student across all nine subjects in terms of overall scores
def best_student():
        query_3 = """SELECT name, MAX(physics + chemistry + mathematics + economics + accounting + 
        english + literature + agriculture + geography)
            FROM waec_scores;
                """
        cursor.execute(query_3)

        rows = cursor.fetchall()
        for row in rows:
            print(f"The best performing student across all subjects is {row[0]} with {row[1]} overall scores")

best_student()

# Who is the best performing student across all nine subjects in term of average scores
def AVG_best_student():
        query_3 = """SELECT name, ROUND(AVG(physics + chemistry + mathematics + economics + accounting 
        + english + literature + agriculture + geography)/9,0)
            FROM waec_scores;
                """
        cursor.execute(query_3)

        rows = cursor.fetchall()
        for row in rows:
            print(f"The student with the best average score across all subjects is {row[0]} with {row[1]} scores")

AVG_best_student()