from src.models.school import School
from src.database.fetch import fetchData

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

def isOption(choice):
    if   0 < choice < 12:
        return True
    return False
    


def evalOperation(school: School, choice):
    
    operations = {
        1: lambda: school.createPerson(),
        2: lambda: school.createClass(),
        3: lambda: school.createSubject(),
        4: lambda: school.assignStudent(),
        6: lambda: fetchData("get_all_persons"), 
        7: lambda: fetchData("get_classes"),
        8: lambda: fetchData("get_subjects"),
        9: lambda: fetchData("get_students_in_class", '8C2')
    }

    if(isOption(choice)):
        operations[choice]()
            



# Entry point to the application
if __name__ == "__main__":

    school = School("  Instituto Federal de Ciência e Tecnologia de Mato Grosso do Sul  ")
    print(school)
    terminal = """
  ╔═══════════════════════════════════════════════════════════╗
  ║                                                           ║
  ║            ✨ WELCOME TO THE SCHOOL SYSTEM! ✨            ║
  ║                                                           ║
  ║            Please select *ONE* option to proceed:         ║
  ║                                                           ║
  ╠═══════════════════════════════════════════════════════════╣
  ║   1. Insert Users (Student/Teacher)                       ║
  ║   2. Insert Class                                         ║
  ║   3. Insert Subject                                       ║
  ║   4. Assign Student to Class                              ║
  ║   5. Assign Teacher to Subject                            ║
  ║   6. List Persons                                         ║
  ║   7. List Classes                                         ║
  ║   8. List Subjects                                        ║
  ║   9. Filter Students by Class                             ║
  ║   10. Filter Teachers by Subject                          ║
  ║   11. Exit                                                ║
  ╠═══════════════════════════════════════════════════════════╣
  ║           Use the number keys to select an option!        ║
  ╚═══════════════════════════════════════════════════════════╝
  """
    print(terminal)
    choice = int(input("Insert the option: "))
    evalOperation(school, choice)    
            
