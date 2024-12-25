from database.connection import connection
from database.cursor import cursor
from sqlite3 import Error


def registerToTable(self, table: str):
        # Here is a object that each key represents an entity on database and each value
        # represents an array with the SQL statement and the values to insert.
        tables = {
                "persons":["INSERT INTO persons (id, name, birth_date, type, sex, address, telephone, email) VALUES(?,?,?,?,?,?,?,?)", (self.id, self.name,
                                                                                                                                        self.birth_date, self.role,
                                                                                                                                        self.sex, self.address, 
                                                                                                                                        self.telephone, self.email)],
                "teachers":["INSERT INTO teachers(id) VALUES(?)", (self.id)],
                "students":["INSERT INTO students(id) VALUES(?)", (self.id)],
                "subjects":["INSERT INTO subjects(id, name, workload, tearcher_id) VALUES (?,?,?,?)", (self.id, self.name, self.workload, self.teacher)],
                "classes": ["INSERT INTO classes(id, name, year) VALUES (?, ?, ?)",(self.id, self.name, self.year)],
                "classTeachers": ["INSERT INTO classStudents(class_id, student_id) VALUES(?, ?)", (self.class_id, self.id)],
                "classStudents": ["INSERT INTO classTeachers(class_id, teacher_id) VALUES(?, ?)", (self.class_id, self.id)]
                }
        
        exec = ""
        data = ()
        if table in tables:
                # SQL statement to handle the operation
                exec = tables[table][0]

                # Data to database 
                data = tables[table][1]

        else:
                return "Table not found"
        
        try:
               # cursor.execute(exec, data)
                connection.commit()
                return "Registered on database."
        
        except Error as e:
                connection.rollback()
                return f"An error has occurred: {e}"



