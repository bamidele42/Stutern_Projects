import sqlite3

conn = sqlite3.connect("sales.db")
#print("created sales database")

# Created cursor object
cursor = conn.cursor()
# print("created cursor object")

# # create inventory table
# cursor.execute("""CREATE TABLE inventory(
#                         ID integer,
#                         name text,
#                         price real,
#                         qty_in_stock integer

# )
# """)

# print("Table created successfully")

# create an inventory list
inventory_list = [(1, "pen", 50.00, 20), (2, "books", 200.00, 30), (3, "diaries", 150.00, 15), (1, "stapler", 500.00, 5), (1, "glue", 150.00, 3),
                  (2, "ink", 100.00, 10), (2, "drawing pin", 80.00, 100), (3, "calculator", 1000.00, 15), (3, "envelope", 150.00, 150),
                  (2, "folder", 200.00, 7), (1, "scissors", 500.00, 15), (3, "eraser", 50.00, 3), (3, "ruler", 120.00, 2), (2, "tape", 180, 1),
                  (3, "pencil", 20.00, 2)]

# Adding values to the inventory table
# cursor.executemany("INSERT INTO inventory VALUES(?,?,?,?)", inventory_list)

# print("Values inserted correctly")

# select from table
cursor.execute("SELECT * FROM inventory")

query = cursor.execute("""SELECT ID, name, price,
         CASE 
            WHEN qty_in_stock > 50 THEN "sufficient"
            WHEN qty_in_stock < 30 THEN "restock"
            ELSE "Do not restock for now"
        END AS items
    FROM inventory
    ORDER BY price DESC;""")

rows = cursor.fetchall()
print(f"ID \t Name \t\t price  Status")
for row in rows:
    print()
    ID, name, price, qty_in_stock = row
    print(f"{ID}\t{name:15}\t{price}\t{qty_in_stock}")






conn.commit()
conn.close()