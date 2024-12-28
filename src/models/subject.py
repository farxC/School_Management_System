from src.models.hours import Hours
from uuid import uuid5
from src.database.insert import insert


class Subject:
    def __init__(self, name: str, id: int, workload: Hours):
        self.name = name
        self.id = id
        self.workload = workload
        self.registerSubject()

    def registerSubject(self):
        insert(self,"subjects")
     
    def __str__(self):
        return f"{self.name} has the teacher {self.teacher}"    

