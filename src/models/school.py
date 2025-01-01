from src.models.hours import Hours
from random import randint
from src.models.person import Student, Teacher
from src.models.subject import Subject
from src.models.grade import Class, assignClass


ALLOWED_ROLES = {"teacher", "student"}

def isValidRole(role: str) -> bool:
    return True if role in ALLOWED_ROLES else False


class School:
    def __init__(self,name, users=[""], classes=[""], subjects=[""]):
        self.name = name
        self.users = users
        self.classes = classes
        self.subjects = subjects
    
        
    def createPerson(self):
        # Mapping possibilities to each Class..
        person_map = {
        "teacher": Teacher,
        "student": Student
        }
        
        name = input("Insert the fullname here: ")
        role = input("What's the role? Teacher or Student?: ").lower()
        address = input("Please inform the complete address: ")
        id = 'P' + str(randint(1,1000)) + role[1].upper()
        sex = input("Insert the gender: ")
        birth_date = input("What day exactly is the person's birth date?: ")
        telephone = input("Inform the telephone here: ")
        email = input("And so.. inform the email (it's the last, I promise): ")

        if isValidRole(role):
           return self.person_map[role](name, role, address, id, sex, birth_date, telephone, email)
   
        raise ValueError("Invalid role!")


    def createClass(self):
        name = input("Insert here the class name: ")
        id = "C" + str(randint(1,10))
        year = input("What's the year of the class? ")
        return Class(name, id, year)

    def createSubject(self):
        name = input("Insert the subject name: ")
        id = "S" + str(randint(10, 100))
        workload = Hours(int(input("What's the time of work that subject does? ")))
        teacher_id = input("Please insert the teacher ID to include in the subject: ")
        return Subject(name, id, workload, teacher_id)
        

    def assignClass(self):
        role = input("Teacher/Student? " ).lower()
        if isValidRole(role):
            p_id = input(f"Insert the {role} ID: ")
            c_id = input("For last, insert the class ID: ")
            return assignClass(p_id, c_id, role)
    
    def __str__(self):
         return f"{self.name}"
    

