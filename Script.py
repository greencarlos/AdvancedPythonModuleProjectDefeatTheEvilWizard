import random
import math


# Parent class
class Character:
    def __init__(self, name, health, attack_power, ability):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.ability = ability

    def attack(self, opponent):
        opponent.health -= math.floor(self.attack_power * random.random())
        print(f"{self.name} attacks with {self.attack_power} power!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special(self, opponent):
        damage = 2 * math.floor(self.attack_power * random.random())
        opponent.health -= damage
        print(f"{self.name} attacks with {damage} power!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25, ability=False)

    def attack(self, opponent):
        damage = math.floor(self.attack_power * random.random())
        opponent.health -= damage
        print(f"{self.name} slashes with a sword, dealing {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special(self, opponent):
        damage = 2 * math.floor(self.attack_power * random.random())
        opponent.health -= damage
        opponent.health -= damage
        print(f"{self.name} went berserk dealing 2x {damage} damage!!!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        self.health += 3
        if self.health > 100:
            self.health = 100
        print(f"{self.name} ate some meat and recovered 3 health points")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, ability=False)

    def attack(self, opponent):
        damage = math.floor(self.attack_power * random.random())
        opponent.health -= damage
        print(f"{self.name} casts a fireball, dealing {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special(self, opponent):
        self.ability = True
        damage = 2 * math.floor(self.attack_power * random.random())
        opponent.health -= damage
        opponent.health -= damage
        opponent.health -= damage
        print(f"{self.name} brings down a meteor dealing 3x {damage} damage!!!")
        print("Divine Shield is enabled, blocking the next attack")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        self.health += 13
        if self.health > 100:
            self.health = 100
        print(f"{self.name} used a healing spell and recovered 13 health points")


class EvilWizard(Character):
    def __init__(self):
        super().__init__(name="Xenanort", health=150, attack_power=15, ability=False)

    def attack(self, opponent):
        if opponent.ability == True:
            opponent.ability = False
            print("Attack missed due to special ability")
        else:
            damage = math.floor(self.attack_power * random.random())
            opponent.health -= damage
            print(f"{self.name} casts a dark energy ball, dealing {damage} damage!")

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerate 5 health! Current health: {self.health}")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=10, ability=False)

    def attack(self, opponent):
        damage = math.floor(self.attack_power * random.random())
        opponent.health -= damage
        print(f"{self.name} shoots an arrow, dealing {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special(self, opponent):
        self.ability = True
        damage = 2 * math.floor(self.attack_power * random.random())
        opponent.health -= damage
        opponent.health -= damage
        print(
            f"{self.name} used quickshot and did an attack with 2x {damage} damage!!!"
        )
        print("Evade is enabled and the next attack will be evaded")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        self.health += 13
        if self.health > 100:
            self.health = 100
        print(f"{self.name} used a and recovered 13 health points")


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=18, ability=False)

    def attack(self, opponent):
        damage = math.floor(self.attack_power * random.random())
        opponent.health -= damage
        print(f"{self.name} slings a stone, dealing {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special(self, opponent):
        damage = math.floor(self.attack_power * random.random())
        opponent.health -= damage
        opponent.health -= damage
        print(f"{self.name} used Holy Strike an attack with 2x {damage} damage!!!")
        print("Evade is enabled and the next attack will be evaded")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        self.health += 11
        if self.health > 100:
            self.health = 100
        print(f"{self.name} used a and recovered 11 health points")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number for your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Archer(name)
    elif class_choice == "4":
        return Paladin(name)
    else:
        print("Invalid choice. Default to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(wizard)
        elif choice == "2":
            player.special(wizard)
        elif choice == "3":
            player.heal()
        elif choice == "4":
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)
            wizard.display_stats()

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")


def main():
    player = create_character()
    wizard = EvilWizard()
    battle(player, wizard)


if __name__ == "__main__":
    main()
