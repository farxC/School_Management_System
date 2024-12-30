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
    

class ClassStudent:
    def __init__(self, student_id, class_id):
        self.student_id = student_id
        self.class_id = class_id
        self.save()
        
    def save(self):
        insert(self, "classStudents") 