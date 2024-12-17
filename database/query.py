from database.connection import connection
from database.cursor import cursor




def fetchData(key: str):
    fetch_keys = {
    "get_all": "SELECT * FROM persons",
    "get_teachers": "SELECT * FROM persons INNER JOIN teachers ON persons.id = teachers.id",
    "get_students": "SELECT * FROM persons INNER JOIN students on persons.id = students.id",
    }

#Inner join that select where person.id = teachers.id (Foreign key).
query ="SELECT * FROM persons p INNER JOIN teachers t ON p.id = t.id "


cursor.execute(query)

res =  cursor.fetchall()

for item in res:
    print(item)
