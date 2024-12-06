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
    
    
    - Utilizar SQLITE
"""

class School:
    def __init__(self, users, classes, subjects):
        self.users = users
        self.classes = classes
        self.subjects = subjects
    
    def __str__(self):
         user_details = "\n".join(str(user) for user in self.users)
         return f"{user_details}"
    

