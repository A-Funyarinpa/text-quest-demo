import random


class Player():
    def __init__(self, starting_health=100, inventory=[ ]):
        # set health
        self.health = starting_health
        self.is_dead = False
        # set starting inventory
        self.inventory = inventory

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        # print("The {} was added to your inventory.".format(item.name))

    def display_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(item.name)
        else:
            print("Your inventory is empty.")

    def discard_broken_items(self):
        for item in self.inventory.copy():
            if item.is_broken:
                self.inventory.remove(item)
                print("The {} was discarded.".format(item.name))

    def weapon_select(self):
        weapons = {}
        for i in range(0, len(self.inventory)):
            if self.inventory[i].is_weapon:
                weapons[i] = self.inventory[i]
        if len(weapons.keys()) >= 1:
            possible_weapons = []
            print("\nSelect your weapon:")
            for i in range(0, len(weapons.keys())):
                possible_weapons.append(str(i + 1))
                print("{} = {}".format(i + 1, weapons[i].name), end=" | ")
            weapon_selected = input("\nPress Enter to confirm selection: ")
            while weapon_selected not in possible_weapons:
                weapon_selected = input("Press Enter to confirm selection: ")
            return weapons[int(weapon_selected) - 1]

    def check_for_death(self):
        if self.health < 1:
            self.is_dead = True

    def get_damaged(self, damage):
        self.health -= damage
        self.check_for_death()

    def check_for_damage(self, enemy_strength):
        damage = 0
        if random.randint(1, 2) == 1:
            damage = enemy_strength * random.randint(1, 10)
            self.get_damaged(damage)
        return str(damage)

    def attack(self, enemy, enemy_strength):
        weapon = self.weapon_select()
        print("""
            You have slain the {}, and you have been hit for {} points of
            damage.""".format(enemy, self.check_for_damage(enemy_strength)))
        weapon.durability_test()
        self.discard_broken_items()

