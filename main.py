from src.models.school import School
from src.models.person import Person, Teacher, Student
from src.models.subject import Subject
from src.models.grade import Class
from src.controllers.personController import createPerson, getPersons
import uuid

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


    
def requirePersonData():
    name = input("Insert the fullname here: ")
    role = input("What's the role? Teacher or Student?: ")
    address = input("Please inform the complete address: ")
    id = str(uuid.uuid4())
    sex = input("Insert the gender: ")
    birth_date = input("What day exactly is the person's birth date?: ")
    telephone = input("Inform the telephone here: ")
    email = input("And so.. inform the email (it's the last, I promise): ")
    dataObject = {
        "name": name,
        "role": role,
        "address": address,
        "id": id,
        "sex": sex,
        "birth_date": birth_date,
        "telephone": telephone,
        "email": email
    }
    return dataObject

def requireClassData():
    name = input("Insert here the class name: ")
    id = str(uuid.uuid4())
    year = input("What's the year of the class?")




def evalOperation(choice):
        
    operations = {
        1: createPerson(requirePersonData()),
        2: requireClassData    
    }

    if(isOption(choice)):
        operations[choice]()
            



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
  ║   2. Insert Class                                         ║
  ║   3. Insert Subject                                       ║
  ║   4. Assign Class to Student                              ║
  ║   5. Assign Subject to Teacher                            ║
  ║   6. List Persons                                         ║
  ║   7. List Classes                                         ║
  ║   8. List Subjects                                        ║
  ║   9. List All                                             ║
  ║   10. Filter Teachers by Subject                          ║
  ║   11. Exit                                                ║
  ╠═══════════════════════════════════════════════════════════╣
  ║           Use the number keys to select an option!        ║
  ╚═══════════════════════════════════════════════════════════╝
  """
    # Funny terminal =)
    print(terminal)
    choice = int(input("Insert the option: "))
    evalOperation(choice)    
            
