from src.school import School
class Class:
    def __init__(self, name, subjects, teachers , students, code ):
        self.name = name
        self.subjects = subjects
        self.teachers = teachers
        self.students = students
        self.code = code

    def __str__(self):
      return f"""
            ****- Class {self.name} -****
            Class code: {self.code}
            Taught by {self.teachers}
            Students: {self.students}
            Subjects: {self.subjects}
        """
    

alg = Class("TADS 1", "", ["Beto", "Vlad", "Huilton", "Kader"], ["Eu"], 1)
