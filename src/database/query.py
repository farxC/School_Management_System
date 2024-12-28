from src.database.connection import connection
from src.database.cursor import cursor




def fetchData(key: str):
    fetch_keys = {
    "get_all": "SELECT * FROM persons",
    "get_teachers": "SELECT * FROM persons INNER JOIN teachers ON persons.id = teachers.id",
    "get_students": "SELECT * FROM persons INNER JOIN students on persons.id = students.id",
    }

#Inner join that select where person.id = teachers.id (Foreign key).
query ="SELECT * FROM persons as p INNER JOIN teachers as t ON p.id = t.id"


cursor.execute(query)

res =  cursor.fetchall()

for item in res:
    print(item)
