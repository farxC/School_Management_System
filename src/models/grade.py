from src.database.insert import insert
from typing import Protocol

class ClassProtocol(Protocol):
    name: str
    id: str
    year: str

class Class:
    def __init__(self, name, id ,year):
        self.name = name
        self.id = id
        self.year = year
        self.__save()
    
    def __save(self):
       query = insert(self, "classes")
       print(query)
       
    def __int__(self):
      return self.id
    

class PersonAssignClass:
    def __init__(self, person_id, class_id, role):
        self.person_id = person_id
        self.class_id = class_id
        self.role = role
        self.__save()
        
    def __save(self):
        tables = {
            "teacher" : "classTeachers",
            "student" : "classStudents" 
        }
        where = tables[self.role]
        query = insert(self, where) 
        print(query)
        
