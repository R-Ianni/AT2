from character import Character

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, "Rogue", armour = 7)
        # Additional attributes and methods specific to the Rogue class
