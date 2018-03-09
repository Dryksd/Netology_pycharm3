class Non_human():
    brain = 2
    tail = 1
    head = 1

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

class Cows(Non_human,Animals):
    mass = 10
class Goats(Non_human,Animals):
    mass = 5
class Sheep(Non_human,Animals):
    mass = 5
class Pigs(Non_human,Animals):
    mass = 6

class Chickens(Non_human,Bird):
    mass = 2
class Gooses(Non_human,Bird):
    mass = 2
class Ducks(Non_human,Bird):
    mass = 1


