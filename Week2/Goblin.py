"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

# class person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone 

#     def greet(self, other_person):
#         print(f"'Hello {self.name}, I am {other_person.name}!'")

#     def print_contact_info(self):
#         print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

# sonny = person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = person("Jordan", "jordan@aol.com", "495-586-3456")

# sonny.greet(jordan)
# jordan.greet(sonny)
# sonny.print_contact_info()
# jordan.print_contact_info()

    # while goblin_health > 0 and hero_health > 0:
    #     print("You have %d health and %d power." % (hero_health, hero_power))
    #     print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
    #     print()
    #     print("What do you want to do?")
    #     print("1. fight goblin")
    #     print("2. do nothing")
    #     print("3. flee")
    #     print("> ",)
    #     user_input = input()
    #     if user_input == "1":
    #         # Hero attacks goblin
    #         goblin_health -= hero_power
    #         print("You do %d damage to the goblin." % hero_power)
    #         if goblin_health <= 0:
    #             print("The goblin is dead.")
    #     elif user_input == "2":
    #         pass
    #     elif user_input == "3":
    #         print("Goodbye.")
    #         break
    #     else:
    #         print("Invalid input %r" % user_input)

    #     if goblin_health > 0:
    #         # Goblin attacks hero
    #         hero_health -= goblin_power
    #         print("The goblin does %d damage to you." % goblin_power)
    #         if hero_health <= 0:
    #             print("You are dead.")





class Hero: 
        def __init__(self, name,  health=10, power=5):
            self.name = name
            self.health = health
            self.power = power
class Goblin: 
        def __init__(self, name, health=6, power=2):
            self.name = name
            self.health = health
            self.power = power

hero = Hero (name="hero", health=10, power=5)
goblin = Goblin (name="goblin", health=6, power=2)
while goblin.health > 0 and hero.health > 0:
  print(f"you have {hero.health} health and {hero.power} power")
  print(f"goblin has {goblin.health} health and {goblin.power} power")
  print("Do you want to.")
  print("1. fight the goblin")
  print("2. do nothing.")
  print("3. run")
  user_input = input()

  if user_input == '1':
    #hero attacks
    goblin.health -= hero.power
    print(f"you do {hero.power} to the goblin")
    # if goblin.health <= 0:
    #           print("The goblin is dead.")
    hero.health -= goblin.power
    print(f"you took {goblin.power} damage")
  elif user_input == '2':
    pass
  elif user_input == '3':
    break
  else: 
    print(f"invalid option {user_input}")
    if goblin.health > 0:
        hero.health -= goblin.power
        print(f"you took {goblin.power} damage")
        if hero.health <= 0:
              print("you are dead.")