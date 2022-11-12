class Hero:  # Template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


Hero1 = Hero("Sniper", 100, 10, 4)
Hero2 = Hero("Miranda", 150, 15, 2)
Hero3 = Hero("Ucup", 200, 5, 1)

print(Hero1.__dict__)
print(Hero2.name)
print(Hero3.health)
