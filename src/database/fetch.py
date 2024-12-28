from src.database.connection import connection
from src.database.cursor import cursor

def fetchData(key: str):
    fetch = {
    "get_all": "SELECT * FROM persons",
    "get_teachers": "SELECT * FROM persons INNER JOIN teachers ON persons.id = teachers.id",
    "get_students": "SELECT * FROM persons INNER JOIN students on persons.id = students.id",
    "get_classes": "SELECT * from classes",
    "get_subjects": "SELECT * from subjects",
    "get_students_in_class": "SELECT * from students as s LEFT JOIN classStudents as cs on s.id = cs.student_id",
    "get_teachers_in_class": "SELECT * from teachers as t LEFT JOIN classTeachers as ct on t.id = ct.teacher_id",
    }
    if key in fetch.keys():
        print("Encountered the key for data fetching")
        q = fetch[key]
        cursor.execute(q)
        res = cursor.fetchall()
        
        for item in res:
            print(item)
        
        return 


