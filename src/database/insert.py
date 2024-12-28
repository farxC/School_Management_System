from src.database.connection import connection
from src.database.cursor import cursor
from sqlite3 import Error


def insert(self, table: str):
            # Here is a object that each key represents an entity on database and each value
            # represents an array with the SQL statement and the values to insert.
            attributes = vars(self)
            
            tables = {
                    "persons":[
                            "INSERT INTO persons (id, name, birth_date, type, sex, address, telephone, email) VALUES(?,?,?,?,?,?,?,?)",
                            lambda obj: (obj["id"], obj["name"], obj["birth_date"], obj["role"], obj["sex"], obj["address"], obj["telephone"], obj["email"])
                    ],
                    "teachers":[
                            "INSERT INTO teachers(id) VALUES(?)",
                            lambda obj: ([obj["id"]])
                    ],
                    "students":[
                            "INSERT INTO students(id) VALUES(?)",
                            lambda obj:([obj["id"]])
                    ],
                    "subjects":[
                            "INSERT INTO subjects(id, name, workload, tearcher_id) VALUES (?,?,?,?)",
                            lambda obj: (obj["id"], obj["name"], obj["workload"], obj["teacher_id"])        
                    ],
                    "classes": [
                            "INSERT INTO classes(id, name, year) VALUES (?, ?, ?)",
                            lambda obj: (obj["id"], obj["name"], obj["year"])],
                    "classTeachers": [
                            "INSERT INTO classStudents(class_id, student_id) VALUES(?, ?)",
                            lambda obj: (obj["class_id"], obj["id"])],
                    "classStudents": [
                            "INSERT INTO classTeachers(class_id, teacher_id) VALUES(?, ?)", 
                            lambda obj: (obj["class_id"], obj["id"])]
            }
            if table not in tables:   
                return "Table not found"
            try:
                
                # # SQL statement to handle the operation
                exec = tables[table][0]
               
                # Data to database 
                data = tables[table][1](attributes)
                print(data)
                cursor.execute(exec, data)
                connection.commit()
                print("Registered on database.")
            
            except Error as e:
                    connection.rollback()
                    return f"An error has occurred: {e}"
