class Hero:
    def __init__(self, name: str, health: int, attackPower: int, armorNumber: int):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):  # Method menyerang # Lawan: object
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(
            self, self.attackPower
        )  # Saat menyerang, lawan otomatis diserang

    def diserang(self, lawan, attackPowerLawan: int):  # Method diserang
        print(f"{self.name} diserang {lawan.name}")
        attackDiterima = attackPowerLawan / self.armorNumber
        self.health -= attackDiterima
        print(f"attack power lawan = {attackPowerLawan}")
        print(f"serangan terasa = {attackDiterima}")
        print(f"darah {self.name} tersisa = {self.health}")


sniper = Hero("sniper", 100, 10, 5)  # Membuat Hero baru
nikimaru = Hero("nikimaru", 120, 7, 8)

sniper.serang(nikimaru)  # Sniper menyerang nikimaru
print("\n")
nikimaru.serang(sniper)
print("\n")
nikimaru.serang(sniper)
print("\n")
nikimaru.serang(sniper)
