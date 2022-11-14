class Hero:
    def __init__(self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        self.__info = (
            f"name {self.__name}:\n\thealth: {self.__health}\n\tarmor: {self.__armor}"
        )

    # def info(self):
    #     data = (
    #         f"name {self.__name}:\n\thealth: {self.__health}\n\tarmor: {self.__armor}"
    #     )
    #     return data
    @property
    def info(self):
        return self.__info

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        print("armor di delete")
        self.__armor = input

    @armor.deleter
    def armor(self):
        self.__armor = None


sniper = Hero("sniper", 100, 10)
print(sniper.info)

print("\nGetter dan setter untuk __armor: ")
print(f"armor = {sniper.armor}")
sniper.armor = 50
print(f"armor = {sniper.armor}")
print("\nDelete armor")
del sniper.armor
print(sniper.__dict__)
