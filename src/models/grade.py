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
        self.registerGrade()
    
    def registerGrade(self):
       q = insert(self, "classes")
       print(q)
       
    def __int__(self):
      return self.id
    

class assignClass:
    def __init__(self, person_id, class_id, role):
        self.person_id = person_id
        self.class_id = class_id
        self.role = role
        self.save()
        
    def save(self):
        tables = {
            "teacher" : "classTeachers",
            "student" : "classStudents" 
        }
        where = tables[self.role]
        q = insert(self, where) 
        print(q)
        
