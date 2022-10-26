import os
import sqlite3

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()

sql_db = '''
    SELECT SUM (UnitPrice) * SUM (Quantity)
        FROM invoice_items;
'''
result = cur.execute(sql_db).fetchall()

for result in result:
    print(*result)

sql_db = '''
    SELECT FirstName
        FROM customers;
'''
print("-" * 50)
result = cur.execute(sql_db).fetchall()
array_d = {}.fromkeys(result, 0)
for a in result:
    array_d[a] += 1
print(array_d)




