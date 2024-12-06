from school import School
from person import me, Person
from hours import Hours

class Discipline:
    def __init__(self, name: str, code: int, workload: Hours, teacher: Person):
        self.name = name
        self.code = code
        self.workload = workload
        self.teacher = teacher
     
    def __str__(self):
        return f"{self.name} has the teacher {self.teacher}"    

if me.isTeacher():
    alg = Discipline("Algoritmos", 1, Hours(80),me)
print(alg)