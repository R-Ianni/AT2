from character import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, "Mage", armour = 5)
        # Additional attributes and methods specific to the Mage class
