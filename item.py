import random


class Item:
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.is_broken = False
        self.is_weapon = False
        self.is_key_item = False
        
    def get_broken(self):
        self.is_broken = True
        print("The {} has broken!".format(self.name))


class Weapon(Item):
    def __init__(self, name, durability=2, weapon_range=1):
        super().__init__(name)
        self.durability = durability
        self.range = weapon_range
        self.is_weapon = True

    def get_damaged(self):
        self.durability -= 1
        if self.durability < 1:
            self.get_broken()

    def durability_test(self):
        durability_check = random.randint(1, 3)
        if durability_check == 1:
            print("\nThe {} was damaged".format(self.name))
            self.get_damaged()


class ColoredStone(Item):
    def __init__(self, name, color):
        super().__init__(name)
        self.is_key_item = True
        self.color = color
        self.is_placed = True

    def interact(self):
        self.is_placed = not self.is_placed
