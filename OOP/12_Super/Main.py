class Hero:
    def __init__(self,name,health):
        self.name=name
        self.health=health

    def info(self):
        print(f"{self.name} mempunyai health: {self.health}")

class HeroIntelligent(Hero):
    def __init__(self,name):
        super().__init__(name,100)
        super().info()

class HeroStrength(Hero):
    def __init__(self,name):
        super().__init__(name,200)
        super().info()

lina=HeroIntelligent('Lina')
namor=HeroStrength('namor')