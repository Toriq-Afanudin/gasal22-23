class Hero:
    # Private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # Method ini hanya berlaku untuk object
    # def getJumlah(self):
    #     return Hero.__jumlah

    # Method ini tidak berlaku untuk object, tapi berlaku untuk class
    # def getJumlah():
    #     return Hero.__jumlah

    # Method static (decorator) nempel ke object dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero("sniper")
print(Hero.getJumlah2())
print(sniper.getJumlah2())
print(Hero.getJumlah3())
print(sniper.getJumlah3())
