# Parent class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def move(self):
        print(f"{self.name} is moving!")

    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power!")

class Warrior(Character):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.armor = armor

    def attack(self):
        print(f"{self.name} slashes with a sword, dealing with {self.attack_power} damage!")

    def use_shield(self):
        print(f"{self.name} blocks the attach with a shield!")


class Mage(Character):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self):
        print(f"{self.name} casts a fireball, dealing {self.attack_power} damage!")

    def cast_spell(self):
        print(f"{self.name} casts a powerful spell!")
