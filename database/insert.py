from database.connection import connection
from database.cursor import cursor
from sqlite3 import Error


def registerToTable(self, insert_table: str):
       
        sql_tables = {
                "persons":["INSERT INTO persons (id, name, birth_date, type, sex, address, telephone, email) VALUES(?,?,?,?,?,?,?,?)", (self.id, self.name,
                                                                                                                                        self.birth_date, self.role,
                                                                                                                                        self.sex, self.address, 
                                                                                                                                        self.telephone, self.email)],
                "teachers":["INSERT INTO teachers(id) VALUES(?)", (self.id,)],
                "students":["INSERT INTO students(id) VALUES(?)", (self.id,)]
                }
        
        exec = ""
        data = ()
        if insert_table in sql_tables:
                print(sql_tables[insert_table])
                exec = sql_tables[insert_table][0]
                data = sql_tables[insert_table][1]
        else:
                return "Table not found"
        
        try:
                cursor.execute(exec, data)
                connection.commit()
                return "Registered on database."
        
        except Error as e:
                connection.rollback()
                return f"An error has occurred: {e}"



