from src.models.person import Person, PersonProtocol, Student, Teacher
from src.database.fetch import fetchData


def createPerson(obj: PersonProtocol):
  
   if obj["role"] == "teacher":
      print("Sorry.. I lied. ")
      subject_id = input("Insert the ID of the teacher subject: ")
      return Teacher(obj["name"], obj["role"], obj["address"], obj["id"], obj["sex"], obj["birth_date"], obj["telephone"], obj["email"], subject_id)
   
   elif obj["role"] == "student":
       print("Sorry.. I lied. ")
       class_id = input("Insert the ID of the student class: ")
       return Student(obj["name"], obj["role"], obj["address"], obj["id"], obj["sex"], obj["birth_date"], obj["telephone"], obj["email"], class_id) 
   
   raise ValueError("Invalid role!")


def getPersons():
    fetchData("get_all")