from typing import Literal
from src.database.insert import insert

"""
    Usuários:
        - Alunos: Nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail.
            ******************************************************************
            - O sistema deve permitir a matricula de alunos em turmas.
        
        - Professores: nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail
            ******************************************************************       
            - O sistema deve permitir a alocação de professores em disciplinas.
"""

Allowed_Roles = Literal["teacher", "student"]
Sex_Options = Literal["masc", "fem"]
ALLOWED_ROLES = {"teacher", "student"}

def isValidRole(role: str) -> bool:
    return True if role in ALLOWED_ROLES else False

class Person: 
        def __init__(self, name: str, role: Allowed_Roles, address: str, id: str, sex: Sex_Options , birth_date: str, telephone: str, email: str):
            self.name = name
            self.role = role.lower()
            self.address = address
            self.id = id
            self.sex = sex
            self.birth_date = birth_date
            self.telephone = telephone
            self.email = email
            # Insert as default to the database.
            self.registerAsPerson()
        
        def registerAsPerson(self):
           insert(self,"persons")
           
        
class Teacher(Person):
    def __init__(self, name: str, role: Allowed_Roles, address: str, id: str, sex: Sex_Options, birth_date: str, telephone: str, email: str, subject_id: int):
        super().__init__(name, role, address, id, sex, birth_date, telephone, email)
        self.subject_id = subject_id
        # Insert as default to the database.
        self.registerAsTeacher()
       
    def registerAsTeacher(self):
       insert(self, "teachers")
        

class Student(Person):
    def __init__(self,name,role, address, id, sex, birth_date, telephone, email , class_id: int):
        super().__init__(name,role,address, id, sex, birth_date, telephone, email)
        self.class_id = class_id
        self.registerAsStudent()
       
    def registerAsStudent(self):
       insert(self, "students")
       
    
  


