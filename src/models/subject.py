from src.models.hours import Hours
from src.database.insert import insert
from typing import Protocol

class SubjectProtocol(Protocol):
    name: str
    id: str
    workload: Hours
    teacher_id: str

class Subject:
    def __init__(self, name: str, id: int, workload: Hours, teacher_id: str):
        self.name = name
        self.id = id
        self.workload = str(workload)
        self.teacher_id = teacher_id
        self.registerSubject()

    def registerSubject(self):
        q = insert(self,"subjects")
        print(q)
       