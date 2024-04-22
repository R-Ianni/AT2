from enemy import Enemy
import random
class Goblin(Enemy):
    MAX_LEVEL = 5

    def __init__(self, level):
        level = min(level, self.MAX_LEVEL)
        super().__init__("Goblin", level, health=20 * level, damage=1 * level)

    def take_damage(self, amount):
        if amount > 0 and self.weakness_to_fire:
            amount *= 2  # Double damage from fire attacks
        super().take_damage(amount)


    def drop_loot(self):
        gold_dropped = random.randint(3, 10)
        return gold_dropped

    @property
    def weakness_to_fire(self):
        return True
