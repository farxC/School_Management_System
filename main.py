from src.school import School
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

# Entry point to the application
if __name__ == "__main__":

    school = School("Instituto Federal de Ciência e Tecnologia de Mato Grosso do Sul")

    terminal = """
  ╔═══════════════════════════════════════════════════════════╗
  ║                                                           ║
  ║            ✨ WELCOME TO THE SCHOOL SYSTEM! ✨            ║
  ║                                                           ║
  ║            Please select *ONE* option to proceed:         ║
  ║                                                           ║
  ╠═══════════════════════════════════════════════════════════╣
  ║   1. Insert Users (Student/Teacher)                       ║
  ║   2. Assign Class to Student                              ║
  ║   3. Assign Subject to Teacher                            ║
  ║   4. List Classes                                         ║
  ║   5. List Subjects                                        ║
  ║   6. List Users                                           ║
  ║   7. List All                                             ║
  ║   8. Filter Teachers by Subject                           ║
  ║   9. Exit                                                 ║
  ╠═══════════════════════════════════════════════════════════╣
  ║           Use the number keys to select an option!        ║
  ╚═══════════════════════════════════════════════════════════╝
  """

    print(terminal)

  

    choice = int(input("Insert the option: "))

    def evaluateChoice(choice: int):
        operations= {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: "",
        }