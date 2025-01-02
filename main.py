from src.models.school import School
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
    if   0 < choice < 11:
        return True
    return False
    

def evalOperation(school: School, choice: int):
    operations = {
        1: lambda: school.createPerson(),
        2: lambda: school.createClass(),
        3: lambda: school.createSubject(),
        4: lambda: school.assignPersonClass(),
        5: lambda: school.assignSubjectClass(),
        6: lambda: school.search("get_all_persons"), 
        7: lambda: school.search("get_classes"),
        8: lambda: school.search("get_subjects"),
        9: lambda: school.search("get_students_in_class", True),
        10: lambda: school.search("get_teachers_in_class", True)
    }
    res = isOption(choice)
    if res:
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
  ║   5. Assign Subject to Class                              ║
  ║   6. List Persons                                         ║
  ║   7. List Classes                                         ║
  ║   8. List Subjects                                        ║
  ║   9. Filter Students by Class                             ║
  ║   10. Filter Teachers by Class                            ║
  ║                                                           ║
  ╠═══════════════════════════════════════════════════════════╣
  ║           Use the number keys to select an option!        ║
  ╚═══════════════════════════════════════════════════════════╝
  """
    print(interface)
    choice = int(input("Insert the option: "))
    proceed = evalOperation(school , choice)
    
    # Recursively call the terminal..
    while proceed:
        terminal(school)
    
    return


# Entry point to the application
if __name__ == "__main__":

    school = School("  Instituto Federal de Ciência e Tecnologia de Mato Grosso do Sul  ")
    print(school)
    terminal(school)
            
