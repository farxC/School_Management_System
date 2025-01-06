from src.database.connection import connection
from src.database.cursor import cursor


def fetchData(key: str, value=None):
    fetch = {
        "get_all_persons": "SELECT * FROM persons",
        "get_teachers": "SELECT * FROM persons as p INNER JOIN teachers as t ON p.id = t.id",
        "get_students": "SELECT * FROM persons RIGHT JOIN students ON persons.id = students.id",
        "get_classes": """
       SELECT c.id, c.name, c.year, p.id, p.type, p.name, p.sex, p.birth_date from classes c INNER JOIN classStudents cs ON c.id = cs.class_id INNER JOIN persons p ON cs.student_id = p.id
       UNION
       SELECT c.id, c.name, c.year, p.id, p.type, p.name, p.sex, p.birth_date from classes c INNER JOIN classTeachers ct on c.id = ct.class_id INNER JOIN persons p ON ct.teacher_id = p.id
       UNION
       SELECT c.id, c.name, c.year, NULL AS id, NULL AS type, NULL AS name, NULL AS sex, NULL AS birth_date FROM classes c;
    """,
        "get_subjects": "SELECT * from subjects",
        "get_students_in_class": "SELECT p.id, p.name, p.type, p.sex, p.email FROM students s INNER JOIN classStudents cs on s.id = cs.student_id INNER JOIN persons p ON p.id = cs.student_id WHERE cs.class_id = ?",
        "get_teachers_in_class": "SELECT p.id, p.name, p.type, p.sex, p.email FROM teachers t INNER JOIN classTeachers ct on t.id = ct.teacher_id INNER JOIN persons p ON p.id = ct.teacher_id  WHERE ct.class_id = ?",
    }
    if key in fetch.keys():
        print("Encountered the key for data fetching")
        q = fetch[key]
        try:
            # Check if provided value argument is not None to execute the parameterized query
            # else execute only the query.
            if value is not None:
                cursor.execute(q, (value,))
            else:
                cursor.execute(q)

            res = cursor.fetchall()

            for item in res:
                print(item)

            return "Query was successful!"
        except Exception as e:
            return "An error has occurred fetching keys: ", e
