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
        self.__save()

    def __save(self):
        q = insert(self,"subjects")
        print(q)

class SubjectAssignClass:
    def __init__(self, subject_id, class_id):
        self.subject_id = subject_id
        self.class_id = class_id
        self.__save()
        
    def __save(self):
        query = insert(self, "classSubjects")
        print(query)