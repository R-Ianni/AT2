
class Enemy:
    def __init__(self, name, level, health, damage, weaknesses=None, resistances=None, gold_drop=0, item_drops=None):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage
        self.weaknesses = weaknesses if weaknesses is not None else []
        self.resistances = resistances if resistances is not None else []
        self.gold_drop = gold_drop
        self.item_drops = item_drops if item_drops is not None else []

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")
        target.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            experience_reward = self.calculate_experience_reward()
            print(f"{self.name} (Level {self.level}) has been defeated! {experience_reward} experience points gained.")


    def calculate_experience_reward(self):
        base_experience = 50  # Base experience reward
        experience_reward = base_experience + (self.level - 1) * 10  # Example formula (adjust as needed)
        return experience_reward


    def is_alive(self):
        return self.health > 0

    def drop_loot(self):
        # Placeholder method for dropping loot
        return 0  # Default to 0 gold dropped
