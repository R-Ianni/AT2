class Orc(Enemy):
    def __init__(self, level):
        super().__init__("Orc", level, health=40 * level, damage=10 * level)

    # Add additional methods or attributes specific to orcs if needed