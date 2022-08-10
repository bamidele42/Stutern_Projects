import sqlite3

conn = sqlite3.connect("sales.db")
#print("created sales database")

# Created cursor object
cursor = conn.cursor()

# Make a selection
cursor.execute("SELECT * FROM inventory")

# Calculate the amount the business owner invested in the procurement of the items.
query = cursor.execute("""SELECT ID, 
                        SUM(price) AS Total_amount
                        FROM inventory
                        GROUP BY ID;
                            """)

rows = cursor.fetchall()
print(f"ID \t Amount")
for row in rows:
    ID, price = row
    print(f"{ID}\t{price}")


# Calculate the average quantity of items in stock.
query_1 = cursor.execute("""SELECT ID, 
                            ROUND(AVG(qty_in_stock),0) AS Average_of_items
                            FROM inventory;
                            """)

rows = cursor.fetchall()
print(f"ID \t Quantity_in_stock")
for row in rows:
    ID, qty_in_stock = row
    print(f"{ID}\t{qty_in_stock}")


# Determine the item with the least quantity in stock
query_2 = cursor.execute("""SELECT ID, name, MIN(qty_in_stock)
                            FROM inventory
                            GROUP BY ID;
                        """)
rows = cursor.fetchall()
print(f"ID \t name \t least_Quantity")
for row in rows:
    ID, name, qty_in_stock = row
    print(f"{ID}\t{name}\t{qty_in_stock}")

# Determine the item with the most quantity in stock
query_3 = cursor.execute("""SELECT ID, name, MAX(qty_in_stock)
                            FROM inventory
                            GROUP BY ID;
                            """)

rows = cursor.fetchall()
print(f"ID \t name \t most_quantity")
for row in rows:
    ID, name, qty_in_stock = row
    print(f"{ID}\t{name:10}\t{qty_in_stock}")