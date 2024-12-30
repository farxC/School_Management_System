from src.database.connection import connection
from src.database.cursor import cursor

def fetchData(key: str, value=[""]):
    fetch = {
    "get_all_persons": "SELECT * FROM persons",
    "get_teachers": "SELECT * FROM persons RIGHT JOIN teachers ON persons.id = teachers.id",
    "get_students": "SELECT * FROM persons RIGHT JOIN students ON persons.id = students.id",
    "get_classes": "SELECT * from classes",
    "get_subjects": "SELECT * from subjects",
    "get_students_in_class": "SELECT * from persons as p JOIN students as s ON p.id = s.id JOIN classStudents",
    "get_teachers_in_class": "SELECT t.* from teachers as t LEFT JOIN classTeachers as ct on t.id = ct.teacher_id where ct.class_id = ?",
    }
    if key in fetch.keys():
        print("Encountered the key for data fetching")
        q = fetch["get_students_in_class"]
        try:
            cursor.execute(q)
            res = cursor.fetchall()
            
            for item in res:
                print(item)
            
            return 
        except Exception as e:
            print("An error has occurred fetching keys: ", e)


