class Hero:  # Template
    # Class variable
    jumlah = 0
    anggota = []

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance variable (atribute)
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        Hero.anggota.append(inputName)
        print(f"Membuat hero dengan nama {inputName}")


Hero1 = Hero("Sniper", 100, 10, 4)
print(Hero.jumlah)
print(Hero.anggota)
Hero2 = Hero("Miranda", 150, 15, 2)
print(Hero.jumlah)
print(Hero.anggota)
Hero3 = Hero("Ucup", 200, 5, 1)
print(Hero.jumlah)
print(Hero.anggota)
