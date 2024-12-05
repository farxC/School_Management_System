from school import School
from person import Person

class Discipline(School):
    def __init__(self, name, code, workload, teacher):
        self.name = name
        self.code = code
        self.workload = workload
        self.teacher = teacher