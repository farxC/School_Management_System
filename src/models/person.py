from typing import Literal
from src.database.insert import insert
from typing import Protocol
import uuid
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

# Defines the interface (shape) of the Person attributes
class PersonProtocol(Protocol):
    name: str
    role: Allowed_Roles
    address: str
    id: str
    sex: Sex_Options
    birt_date: str
    telephone: str
    email: str


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
            self.save()
            
        
        def save(self):
           q = insert(self,"persons")
           print(q)
        
class Teacher(Person):
    def __init__(self, name: str, role: Allowed_Roles, address: str, id: str, sex: Sex_Options, birth_date: str, telephone: str, email: str, subject_id = None):
        super().__init__(name, role, address, id, sex, birth_date, telephone, email)
        self.subject_id = subject_id
        self.save_teacher()
        
        
    def save_teacher(self): 
       q =insert(self, "teachers")
       print(q)

class Student(Person):
    def __init__(self,name,role, address, id, sex, birth_date, telephone, email , class_id = None):
        super().__init__(name,role,address, id, sex, birth_date, telephone, email)
        self.class_id = class_id
        self.save_student()
       
    def save_student(self):
      q = insert(self, "students")