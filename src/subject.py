from src.school import School
from src.person import me, Person
from src.hours import Hours
from uuid import uuid5

class Subject:
    def __init__(self, name: str, id: int, workload: Hours):
        self.name = name
        self.id = id
        self.workload = workload
       
     
    def __str__(self):
        return f"{self.name} has the teacher {self.teacher}"    

if me.isTeacher():
    alg = Subject("Algoritmos", 1, Hours(80))
