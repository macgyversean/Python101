class Character:
    def __init__(self, health):
          self.health = health 
       #    good to go
    def alive(self):
            return self.health > 0

    def attack(self, enemy):
                enemy.health -= self.power
                print(f"{self.name} did {self.power} damage")
                if enemy.health <= 0:
                      print(f"{enemy.name} is dead")

    def print_status_of_hero(self):
                print( f"{self.name} has {self.power} damage and {self.name} has {self.health} health .") 


class Hero(Character): 
    def __init__(self, health, power, name):
            self.health = health
            self.power = power
            self.name = name
        
class Goblin(Character): 
        def __init__(self, health, power, name):
            self.health = health
            self.power = power
            self.name = name
hero = Hero(10, 5, "Spiderman")
goblin = Goblin(6, 2, " green goblin")

while goblin.alive() and hero.alive():
        hero.print_status_of_hero() 
        goblin.print_status_of_hero()
        print("What do you want to do?")
        print(f"1. fight {goblin.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1": 
             hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {user_input}")
        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)

