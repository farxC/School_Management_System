from database.connection import connection, cursor

query ="SELECT * FROM persons WHERE id=1"

cursor.execute(query)

res =  cursor.fetchall()
for item in res:
    print(item)
