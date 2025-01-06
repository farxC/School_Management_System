from src.models.school import School
from flask import Flask

"""
- Crie um sistema escolar que permita cadastrar alunos, professores, disciplinas e turmas.
    Usuários:
        - Alunos: Nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail.
            ******************************************************************
            - O sistema deve permitir a matricula de alunos em turmas.
        
        - Professores: nome, matrícula, data de nascimento, sexo, endereço, telefone e e-mail
            ******************************************************************       
            - O sistema deve permitir a alocação de professores em disciplinas.
                        
    - Disciplinas: nome, código, carga horária, professor.
    - Turmas: nome, código (A1234), disciplina, professor, alunos (lista-matricula)

    - O sistema deve permitir a filtragem de professores por disciplina.
"""

app = Flask(__name__)

@app.route("/")
def index():
        return "<h1>School System</h1"

@app.route('/hello')
def hello():
    return "Hello, world"
    



# Entry point to the application
if __name__ == "__main__":
  
    app.run(debug=True)


