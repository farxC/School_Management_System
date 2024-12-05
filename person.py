from typing import Literal
import sqlite3

ALLOWED_ROLES = Literal["teacher", "student"]

def isValidRole(role: str) -> bool:
     return role in ALLOWED_ROLES

"""
    Usuários:
        - Alunos: Nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail.
            ******************************************************************
            - O sistema deve permitir a matricula de alunos em turmas.
        
        - Professores: nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail
            ******************************************************************       
            - O sistema deve permitir a alocação de professores em disciplinas.
"""

class Person: 
        def __init__(self, name, type, address, registration, sex, birth_date, telephone, email):
            self.name = name
            self.type = type
            self.address = address
            self.registration = registration
            self.sex = sex
            self.birth_date = birth_date
            self.telephone = telephone
            self.email = email
        
        def __str__(self):
            return self.name +" "+ self.type+" " + self.address

        def assing(self):
             pass

        def register(self):
            if isValidRole(self.type):
                 if(self.type) == "Teacher":
                    #To do..  assign()
                    pass
                 else:
                      pass
        
        def show(self):
            print(self.name, self.type)



    
me = Person("Rafael", "Teacher", "Rua tal", "1212121", "masc", "12/01/1999", '','')

