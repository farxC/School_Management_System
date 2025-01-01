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
                        
    - Disciplinas: nome, código, carga horária, professor.
    - Turmas: nome, código (A1234), disciplina, professor, alunos (lista-matricula)

    - O sistema deve permitir a filtragem de professores por disciplina.
"""


def isOption(choice):
    if   0 < choice < 12:
        return True
    return False
    

def evalOperation(school: School, choice: int):
    operations = {
        1: lambda: school.createPerson(),
        2: lambda: school.createClass(),
        3: lambda: school.createSubject(),
        4: lambda: school.assignClass(),
        5: lambda: fetchData("get_all_persons"), 
        6: lambda: fetchData("get_classes"),
        7: lambda: fetchData("get_subjects"),
        # Refatorar essa parte para que NÃO fique hardcoded os values..
        8: lambda: fetchData("get_students_in_class","C6"),
        9: lambda: fetchData("get_teachers_in_class", "C7")
    }

    if(isOption(choice)):
        if choice < 11:
            operations[choice]()
            return True



def terminal(school: School):
    interface = """
  ╔═══════════════════════════════════════════════════════════╗
  ║                                                           ║
  ║            ✨ WELCOME TO THE SCHOOL SYSTEM! ✨            ║
  ║                                                           ║
  ║            Please select *ONE* option to proceed:         ║
  ║                                                           ║
  ╠═══════════════════════════════════════════════════════════╣
  ║   1. Insert Person                                        ║
  ║   2. Insert Class                                         ║
  ║   3. Insert Subject                                       ║
  ║   4. Assign Person to Class                               ║
  ║   5. List Persons                                         ║
  ║   6. List Classes                                         ║
  ║   7. List Subjects                                        ║
  ║   8. Filter Students by Class                             ║
  ║   9. Filter Teachers by Subject                           ║
  ║   10. Exit                                                ║
  ╠═══════════════════════════════════════════════════════════╣
  ║           Use the number keys to select an option!        ║
  ╚═══════════════════════════════════════════════════════════╝
  """
    print(interface)
    choice = int(input("Insert the option: "))
    proceed = evalOperation(school , choice)
    
    # Recursively call the terminal..
    if proceed:
        terminal(school)
    
    return


# Entry point to the application
if __name__ == "__main__":

    school = School("  Instituto Federal de Ciência e Tecnologia de Mato Grosso do Sul  ")
    print(school)
    terminal(school)
            
