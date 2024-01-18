class Person:
    def __init__(self, name, email, phone, print_contact_info):
      self.name = name
      self.email = email
      self.phone = phone
      self.print = print_contact_info

    def greet(self, other_person):
     return 'Hello %s, I am %s!' % (other_person.name,  self.name)
            
    def print_contact_info(self):
       print(Sonny.email, Sonny.phone)
       

    def contact(self):
        print(' %s, %s' % ( self.email, self.phone))
    
    def cont(self):
        print(' %s %s, %s' % ( self.name, self.email, self.phone))


Sonny = Person(name="Sonny", email='sonny@hotmail.com', phone='483-485-4948', print_contact_info='sonny@hotmail.com, 483-485-4948')
Jordan = Person(name= 'Jordan', email= 'jordan@aol.com', phone='495-586-3456',print_contact_info= 'jordan@aol.com, 495-586-3456')

print(Sonny.greet(Jordan))
print(Jordan.greet(Sonny))
print(Sonny.email, Sonny.phone)
print(Jordan.name, Jordan.phone, Jordan.email)
Sonny.print_contact_info()
