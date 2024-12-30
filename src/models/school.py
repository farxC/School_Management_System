"""
- Crie um sistema escolar que permita cadastrar alunos, professores, disciplinas e turmas.
    Usuários:
        - Alunos: Nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail.
            ******************************************************************
            - O sistema deve permitir a matricula de alunos em turmas.
        
        - Professores: nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail
            ******************************************************************       
            - O sistema deve permitir a alocação de professores em disciplinas.
                        
    - Disciplinas: nome, código (UUID), carga horária, professor.
    - Turmas: nome, código (A1234), disciplina, professor, alunos (lista-matricula)

    - O sistema deve permitir a filtragem de professores por disciplina.
"""
from src.models.hours import Hours
import uuid
from random import randint
from src.models.person import Student, Teacher
from src.models.subject import Subject
from src.models.grade import Class, ClassStudent
from src.database.insert import insert

class School:
    def __init__(self,name, users=[""], classes=[""], subjects=[""]):
        self.name = name
        self.users = users
        self.classes = classes
        self.subjects = subjects
        
    def createPerson(self):
        name = input("Insert the fullname here: ")
        role = input("What's the role? Teacher or Student?: ").lower()
        address = input("Please inform the complete address: ")
        id = str(randint(1,10000))
        print(id)
        sex = input("Insert the gender: ")
        birth_date = input("What day exactly is the person's birth date?: ")
        telephone = input("Inform the telephone here: ")
        email = input("And so.. inform the email (it's the last, I promise): ")

        if role == "teacher":
            return Teacher(name, role, address, id, sex, birth_date, telephone, email)
   
        elif role == "student":
            return Student(name, role, address, id, sex, birth_date, telephone, email) 
   
        raise ValueError("Invalid role!")


    def createClass(self):
        name = input("Insert here the class name: ")
        id = "C".join(str(randint(1,100)))
        year = input("What's the year of the class? ")
        return Class(name, id, year)

    def createSubject(self):
        name = input("Insert the subject name: ")
        id = "S".join(str(randint(10, 1000)))
        workload = Hours(int(input("What's the time of work that subject does? ")))
        teacher_id = input("Insert the teacher ID responsible for that subject: ")
        return Subject(name, id, workload, teacher_id)
        

    def assignStudent(self):
        student_id = input("Please insert the student ID: ")
        grade = input("Insert the class ID to assign: ")
        student_assign = ClassStudent(grade, student_id)
        insert(student_assign, "classStudents")
        

    def assignTeacher(self):
        id = input("Please insert the teacher ID: ")
        subject = input("Inform the name or ID from the subject to assign: ")
        insert({id, subject}, "classTeacher")

    
    def __str__(self):
         return f"{self.name}"
    

