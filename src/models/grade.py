from src.database.insert import insert
from typing import Protocol

class ClassProtocol(Protocol):
    name: str
    id: str
    year: str

class Class:
    def __init__(self, name, id ,year,subjects, teacher , students):
        self.name = name
        self.id = id
        self.year = year
        self.subjects = subjects
        self.teacher = teacher
        self.students = students
        self.registerGrade()
    
    def registerGrade(self):
        insert(self, "classes")

    def __int__(self):
      return self.id
    

