from src.models.person import Person, Student, Teacher


def createPerson(name: str, role, address, id, sex, birth_date, telephone, email):
   if role == "teacher":
      print("Sorry.. I lied. ")
      subject_id = input("Insert the ID of the teacher subject: ")
      return Teacher(name, role, address, id, sex, birth_date, telephone, email, subject_id)
   elif role == "student":
       print("Sorry.. I lied. ")
       class_id = input("Insert the ID of the student class: ")
       return Student(name, role, address, id, sex, birth_date, telephone, email, class_id) 
   else:
       raise ValueError("Invalid role!")

person1 = createPerson("Rafael Ortiz Nunes", "teacher", "Rua tal", 28, "masc", "28/03/2000", "(11)-11111", "some@email")
print(person1.name)
print(isinstance(person1, Person))
