class NonHuman:
    brain = 2
    tail = 1
    head = 1


class Animals(NonHuman):
    legs = 4

    def power(self, meal):
        self.meal = meal
        if meal > 0:
            self.strong = meal*2
            return self.strong


class Bird(NonHuman):
    def __init__(self):
        self.legs = 2

    def power(self, meal):
        if meal > 0:
            self.strong = meal*1.5
            return self.strong


class Cows(Animals):
    mass = 10


class Goats(Animals):
    mass = 5


class Sheep(Animals):
    mass = 5


class Pigs(Animals):
    mass = 6


class Chickens(Bird):
    mass = 2


class Gooses(Bird):
    mass = 2


class Ducks(Bird):
    mass = 1