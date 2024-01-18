class Person:
    def __init__(self, name, email, phone):
      self.name = name
      self.email = email
      self.phone = phone

class Sonny:
     def __init__(self, name, email, phone_number):
        super().__init__(self, name, email, phone_number)
        self.name = Sonny
        self.email = "sonny@hotmail.com"
        self.phone_number = "483-485-4948"

class Jordan:
     def __init__(self, name, email, phone_number):
        super().__init__(self, name, email, phone_number)
        self.name = Jordan
        self.mail = "jordan@aol.com"
        self.phone_number = "495-586-3456"

            
def greet(Jordan, Sonny):
      print('Hello %s, I am %s!' % (Jordan, Sonny))

def greet(Sonny, Jordan):
      print('Hello %s, I am %s!' % (Sonny, Jordan))

print(Sonny("%s, %s " % (self.email, self.phone_number)))

