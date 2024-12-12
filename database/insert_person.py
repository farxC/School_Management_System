from connection import conn
from cursor import cursor

def registerToDatabase(self):
            sql = f"INSERT INTO persons (id, name, birth_date, type, sex, address, telephone, email) \
                    VALUES({self.id},{self.name}, {self.birth_date}, {self.role}, {self.sex}, {self.sex}, {self.address}, {self.telephone}, {self.email})"

            cursor.execute(sql)
            conn.commit()
            conn.close()
            return "Person admitted to the sys"
        