from typing import Literal
import database.insert_person
print (database)

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
        def __init__(self, name: str, grade: str, role: Allowed_Roles, address: str, id: str, sex: Sex_Options , birth_date: str, telephone: str, email: str):
            self.name = name
            self.grade = grade
            self.role = role.lower()
            self.address = address
            self.id = id
            self.sex = sex
            self.birth_date = birth_date
            self.telephone = telephone
            self.email = email
        
        def __str__(self):
            return f"{self.name}" 
             
            
        def registerPerson(self):
            registerToDatabase(self)

        def isTeacher(self):
            if isValidRole(self.role):
                 if self.role == "teacher":
                     return True
                 return False
            else:
                return f"Not a valid role, {ALLOWED_ROLES}"    
                 
                
    
me = Person("'Rafael'","'TADS 1'","'teacher'", "'Rua tal'", "'1212121'", "'masc'", "'12/01/1999'", "'(67)11111111'", "'meuemail@email.com'")
me.registerPerson()