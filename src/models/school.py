from src.models.hours import Hours
from random import randint
from src.models.person import Student, Teacher
from src.models.subject import Subject, SubjectAssignClass
from src.models.grade import Class, PersonAssignClass
from typing import Literal

ALLOWED_ROLES = {"teacher", "student"}


def isValidRole(role: str) -> bool:
    return True if role in ALLOWED_ROLES else False


class School:
    def __init__(self, name):
        self.name = name

    __FETCH_KEYS_OPTIONS = Literal[
        "get_all_persons",
        "get_teachers",
        "get_persons",
        "get_classes",
        "get_subjects",
        "get_students_in_class",
        "get_teachers_in_class",
    ]

    def __save(self, object: Class, table: str):
        q = ''
        print(q)

    def createPerson(self):
        # Mapping possibilities to each Class..
        person_map = {"teacher": Teacher, "student": Student}

        name = input("Insert the fullname here: ")
        role = input("What's the role? Teacher or Student?: ").lower()
        address = input("Please inform the complete address: ")
        id = "P" + str(randint(1, 1000)) + role[0].upper()
        sex = input("Insert the gender: ")
        birth_date = input("What day exactly is the person's birth date?: ")
        telephone = input("Inform the telephone here: ")
        email = input("And so.. inform the email (it's the last, I promise): ")

        if isValidRole(role):
            # Mapping person to related table
            tables = {"teacher": "teachers", "student": "students"}

            person = person_map[role](
                name, role, address, id, sex, birth_date, telephone, email
            )

            related_table = tables[role]
            
            # Saving into the table "persons"
            self.__save(person, "persons")
            
            # Saving person to its related role table
            self.__save(person, related_table)

            return person

        raise ValueError("Invalid role!")

    def createClass(self):
        name = input("Insert here the class name: ")
        id = "C" + str(randint(1, 100))
        year = input("What's the year of the class? ")
        grade = Class(name, id, year)

        # Saving into table 'classes'
        self.__save(grade, "classes")

        return grade

    def createSubject(self):
        name = input("Insert the subject name: ")
        id = "S" + str(randint(10, 100))
        workload = Hours(int(input("What's the time of work that subject does? ")))
        teacher_id = input("Please insert the teacher ID to include in the subject: ")
        subject = Subject(name, id, workload, teacher_id)

        # Saving into table 'subjects'
        self.__save(subject, "subjects")

        return subject

    def assignPersonClass(self):

        # Table for mapping each role and related role table.
        tables = {"teacher": "classTeachers", "student": "classStudents"}

        role = input("Teacher/Student? ").lower()
        if isValidRole(role):
            p_id = input(f"Insert the {role} ID: ").upper()
            c_id = input("For last, insert the class ID: ").upper()
            
            assignedPerson = PersonAssignClass(p_id, c_id)
            
            related_table = tables[role]
            
            # Saving person to its related role table
            self.__save(assignedPerson, related_table)
            
            return assignedPerson
        
    def assignSubjectClass(self):
        s_id = input("Please insert the subject ID: ").upper()
        c_id = input("Please insert the class ID: ").upper()

        assignedSubject = SubjectAssignClass(s_id, c_id)

        # Saving into the table "classSubjects"
        self.__save(assignedSubject, "classSubjects")

        return assignedSubject

    def search(self, key: __FETCH_KEYS_OPTIONS, classID=False):
        if classID:
            val = input("Please insert the class ID: ").upper()

    def __str__(self):
        return f"{self.name}"
