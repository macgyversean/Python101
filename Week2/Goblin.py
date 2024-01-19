"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
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
    if goblin.health <= 0:
        print("The goblin is dead.")
  elif user_input == '2':
    pass
  elif user_input == '3':
    print("You ran away like a little baby... Goodbye")
    break
  if goblin.health > 0:
        hero.health -= goblin.power
        print(f"you took {goblin.power} damage")
        if hero.health <= 0:
              print("you are dead.")
  else: 
    print(f"invalid option {user_input}")