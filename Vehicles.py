class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def info(self):
        print('%s %s %s ' % (self.year, self.make, self.model ))

car = Vehicle(year='2015', make='Nissan', model='Leaf', )
print(car.info())    