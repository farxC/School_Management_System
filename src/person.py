from typing import Literal
from database.insert import registerToTable
from src.grade import Class

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
            registerToTable(self, "persons")
        
        def __str__(self):
            return f"{self.name}, {self.id}" 
        
class Teacher(Person):
    def __init__(self, name: str, role: Allowed_Roles, address: str, id: str, sex: Sex_Options, birth_date: str, telephone: str, email: str, subject_id: int):
        super().__init__(name, role, address, id, sex, birth_date, telephone, email)
        self.subject_id = subject_id
        if role in ALLOWED_ROLES:
            registerToTable(self, "teacher")
        
        

class Student(Person):
    def __init__(self,name,role, address, id, sex, birth_date, telephone, email , class_id: int):
        super().__init__(name,role,address, id, sex, birth_date, telephone, email)
        self.class_id = class_id
        if role in ALLOWED_ROLES:
            registerToTable(self, "student")
    
    def __str__(self):
        return f"{self.class_id}"


        

tads1 = Class("TADS1", 1, 1000, [], '','')


person = Student("Reginald", "student","Endereço x", 2, "masc", "19/02/1900", "(11-12121212)", "some@email", int(tads1))

print(person)