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

    # Void function, method tanpa return, tanpa argumen
    def siapa(self):
        print(f"Namaku adalah {self.name}")

    # Method dengan argumen, tanpa return
    def healthUp(self, up):
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health


Hero1 = Hero("Sniper", 100, 10, 4)
Hero2 = Hero("Miranda", 150, 15, 2)
Hero3 = Hero("Ucup", 200, 5, 1)

Hero1.siapa()
Hero1.healthUp(10)
print(Hero1.getHealth())
