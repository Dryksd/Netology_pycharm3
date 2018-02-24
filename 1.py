class Non_human():
    brain = 2

class Animals(Non_human):
    def __init__(self):
        self.legs = 4

    def power(self, meal):
        if meal > 0:
            self.strong = meal*2
            return self.strong

class Bird (Non_human):
    def __init__(self):
        self.legs = 2

    def power (self, meal):
        if meal > 0:
            self.strong = meal*1.5
            return self.strong

cows = Animals()
goats = Animals()
sheep = Animals()
pigs = Animals()

chickens = Bird()
gooses = Bird()
ducks = Bird()

print(cows.power(2))
