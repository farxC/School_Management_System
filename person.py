from school import School
types = ["Teacher", "Student"]

class Person(School):

        def __init__(self, name, type: types, address, registration, sex, birthday, telephone, email):
            self.name = name
            self.type = type
            self.address = address
            self.registration = registration
            self.sex = sex
            self.birthday = birthday
            self.telephone = telephone
            self.email = email
            
        def __str__(self):
            return self.name + self.type    

        def cadastrar(self):
            if self.type == self.types[0]:
               print(self.type) 
        
        def show(self):
            print(self.name, self.type)

        
        
me = Person("Rafael", "Teacher")