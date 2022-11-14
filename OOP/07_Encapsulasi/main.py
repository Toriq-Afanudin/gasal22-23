class Hero:
    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # Getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # Setter
    def diserang(self, serangPower):
        self.__health -= serangPower


# Awal dari game
earthshaker = Hero("earthshaker", 100, 5)
print(earthshaker.__dict__)

# Game berjalan
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())
