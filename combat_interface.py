import pygame as py
from character import Character

class CombatGUI:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.root = pygame
        self.root.title("Combat")
        self.attack_buttons = []
        self.create_widgets()
        self.update_widgets()

    def create_widgets(self):
        self.player_label = tk.Label(self.root, text=f"{self.player.name} (HP: {self.player.current_hp})")
        self.player_label.pack()
        self.enemy_label = tk.Label(self.root, text=f"{self.enemy.name} (HP: {self.enemy.current_hp})")
        self.enemy_label.pack()
        for attack, info in self.player.attacks.items():
            button = tk.Button(self.root, text=f"{attack} (Stamina cost: {info['stamina_cost']})", command=lambda attack=attack: self.player_choose_attack(attack))
            button.pack()
            self.attack_buttons.append(button)
        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack()

    def update_widgets(self):
        self.player_label.config(text=f"{self.player.name} (HP: {self.player.current_hp})")
        self.enemy_label.config(text=f"{self.enemy.name} (HP: {self.enemy.current_hp})")
        for button, (attack, info) in zip(self.attack_buttons, self.player.attacks.items()):
            button.config(text=f"{attack} (Stamina cost: {info['stamina_cost']})", state=tk.NORMAL if self.player.current_stamina >= info["stamina_cost"] else tk.DISABLED)

    def player_choose_attack(self, attack):
        attack_info = self.player.attacks[attack]
        if self.player.current_stamina >= attack_info["stamina_cost"]:
            self.player.current_stamina -= attack_info["stamina_cost"]
            attack_method = attack_info["method"]
            attack_method(self.enemy)
            self.message_label.config(text=f"Player attacks {self.enemy.name} with {attack}!")
            if not self.enemy.is_alive():
                self.message_label.config(text=f"{self.enemy.name} has been defeated!")
                self.root.after(1000, self.root.destroy)
                return
            self.enemy_attack()
        else:
            self.message_label.config(text="Not enough stamina for this attack.")
        self.update_widgets()

    def enemy_attack(self):
        enemy_damage = self.enemy.attack(self.player)
        self.message_label.config(text=f"{self.enemy.name} attacks {self.player.name} for {enemy_damage} damage!")
        if not self.player.is_alive():
            self.message_label.config(text=f"{self.player.name} has been defeated!")
            self.root.after(1000, self.root.destroy)
    def mainloop(self):
        while True:
            

def combat_demo():
    player = Warrior("Player")
    enemy = Goblin(level=3)
    gui = CombatGUI(player, enemy)
    gui.root.mainloop()

if __name__ == "__main__":
    combat_demo()