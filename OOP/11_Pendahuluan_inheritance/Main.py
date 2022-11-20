class Hero:
    def __init__(self,name,health):
        self.name=name
        self.health=health

class HeroIntelligent(Hero):
    pass

class HeroStrength(Hero):
    pass

lina=Hero('lina',100)
axe=HeroIntelligent('axe',50)
namor=HeroStrength('namor',200)

print(lina.name,lina.health)
print(axe.name,axe.health)
print(namor.name,namor.health)