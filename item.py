import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, weight):
        self.name = name
        self.desc = desc
        self.weight = weight
        self.loc = None
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

class Pistol(Item):
    health = '-50'
    prob = None
    def __init__(self):
        Item.__init__(self, "Pistol", "A .357 Magnum Revolver", 2)

class Leaf(Item):
    def __init__(self):
        Item.__init__(self,"Leaf", "This is just a leaf.",1)

class Rock(Item):
    def __init__(self):
        Item.__init__(self,"Rock", "This is just a rock.",15)        

class Boulder(Item):
    def __init__(self):
        Item.__init__(self,"Boulder", "A large boulder.",150)

class Sword(Item): 
    def __init__(self):
        self.health = '-40'
        Item.__init__(self, "Sword", "A long steel broadsword", 10)
        
class Dagger(Item):
    health = '-15'
    prob = None
    def __init__(self):
        Item.__init__(self, "Dagger", 'A short dagger with emeralds embedded in the hilt', 1)
        
class Stick(Item): 
    health = '-10'
    prob = None
    def __init__(self):
        Item.__init__(self, 'Stick', 'A long branch from an oak tree. It is just a stick', 2)
        
class Armor(Item):
    health = '+50'
    prob = None
    def __init__(self):
        Item.__init__(self, "Armor", "Dinosaur scale armor harvested from stegosaurus plates", 20)
  
