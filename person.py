class Person:
    def __init__(self, name, email, phone):
      self.name = name
      self.email = email
      self.phone = phone

    def greet(self, other_person):
     print('Hello %s, I am %s!' % (other_person.name, self.name))

    def contact_info(self):
        print(' %s, %s' % ( self.email, self.phone))
    
    def cont_info(self):
        print(' %s %s, %s' % ( self.name, self.email, self.phone))


Sonny = Person(name="Sonny", email='sonny@hotmail.com', phone='483-485-4948')
Jordan = Person(name= 'Jordan', email= 'jordan@aol.com', phone='495-586-3456')

print(Sonny.greet(Jordan))
print(Jordan.greet(Sonny))
print(Sonny.email, Sonny.phone)
print(Jordan.name, Jordan.phone, Jordan.email)