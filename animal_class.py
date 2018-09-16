# classes_in_python
class Animal:
    def __init__(self, tail, paw, wool):
        self.tail = tail
        self.paw = paw
        self.wool = wool


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, tail=1, paw=4, wool=True)

    def say(self):
        return "Dod say: 'woof-woof'"


dog1 = Dog()
print(dog1.tail, dog1.paw)
print(dog1.say())


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, tail=1, paw=4, wool=True)

    def cat_say(self):
        return "Cat say: 'meow-meow'"

cat1 = Cat()
print(cat1.cat_say())


class SphynxCat(Animal):
    def __init__(self, wool=None):
        Animal.__init__(self, tail=1, paw=4, wool=True)
        self.wool = wool

    def sph_say(self):
        return "Sphynx say: 'murr-murr'"

sphynx = SphynxCat()
print(sphynx.wool)
print(sphynx.sph_say())


class Rooster(Animal):
    def __init__(self, paw=2, wool=False):
        Animal.__init__(self, tail=1, paw=4, wool=True)
        self.paw = paw
        self.wool = wool

    def roost_say(self):
        return "Rooster say: 'Cocorico'"

roost = Rooster()
print(roost.paw, roost.wool)
print(roost.roost_say())







