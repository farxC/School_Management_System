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
  
       
    def __int__(self):
      return self.id
    

class PersonAssignClass:
    def __init__(self, person_id, class_id,):
        self.person_id = person_id
        self.class_id = class_id