class Hero:
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPowerLawan):
        print(self.name + " diserang " + lawan.name)
        attackDiterima = attackPowerLawan / self.armorNumber
        self.health -= attackDiterima
        print(f"attack power lawan = {attackPowerLawan}")
        print(f"serangan terasa = {attackDiterima}")
        print(f"darah {self.name} tersisa = {self.health}")


sniper = Hero("sniper", 100, 10, 5)
nikimaru = Hero("nikimaru", 120, 7, 8)

sniper.serang(nikimaru)
print("\n")
nikimaru.serang(sniper)
print("\n")
nikimaru.serang(sniper)
print("\n")
nikimaru.serang(sniper)
