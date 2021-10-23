class Player():
    def __init__(self, starting_health=100, stats={ }, inventory=[ ]):
        # set health
        self.health = starting_health
        # set stats
        if stats:
            self.strength = stats["strength"]
            self.charisma = stats["charisma"]
            self.stealth = stats["stealth"]
            self.luck = stats["luck"]
        # set starting inventory
        self.inventory = inventory

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print("The {} was added to your inventory.".format(item.name))

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

    def attack(self, weapon):
        if weapon in self.inventory:
            print("Attacked with the {}.".format(weapon.name))
            weapon.durability_test()
            self.discard_broken_items()
        else:
            print("Weapon not in inventory. Please select another/")
