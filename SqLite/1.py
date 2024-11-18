import sqlite3

conn = sqlite3.connect('test.db')

# Create Cursor

cursor = conn.cursor()

# Create a Table
# cursor.execute("""
#     CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
               
#     )

# """)
# many_customers = [
#                     ('wes','brown','wes@brown.com'),
#                     ('kas','patte','kas@patte.com'),
#                     ('john','lawren','john@lauren.com'),
#                 ]
# cursor.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)
cursor.execute(" SELECT rowid, * FROM customers")


# print(cursor.fetchone()[2])


# cursor.fetchmany(3)

# cursor.fetchall()

for i in cursor.fetchall ():
    print(i)

print("Successfully fetch")

conn.commit()

conn.close()
