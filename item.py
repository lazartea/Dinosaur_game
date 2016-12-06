import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, weight,impact):
        self.name = name
        self.desc = desc
        self.weight = weight
        self.impact = impact
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
        Item.__init__(self, "Pistol", "A .357 Magnum Revolver", 30,-25)

class Cigarette(Item):
    def __init__(self):
        Item.__init__(self,"Cigarette","A Cigarette.",1,-5)

class Leaf(Item):
    def __init__(self):
        Item.__init__(self,"Leaf", "Food can increase your health.",1,1)

class Rock(Item):
    def __init__(self):
        Item.__init__(self,"Rock", "This is just a rock.",15,-3)        

class Boulder(Item):
    def __init__(self):
        Item.__init__(self,"Boulder", "A large boulder.",150,-25)

class Sword(Item): 
    def __init__(self):
        
        Item.__init__(self, "Sword", "A long steel broadsword", 20,-40)
        
class Dagger(Item):
    def __init__(self):
        Item.__init__(self, "Dagger", 'A short dagger with emeralds embedded in the hilt', 10,-15)
        
class Stick(Item): 
    def __init__(self):
        Item.__init__(self, 'Stick', 'A long branch from an oak tree. It is just a stick', 2,-10)
        
class Armor(Item):
    def __init__(self):
        Item.__init__(self, "Armor", "Dinosaur scale armor harvested from stegosaurus plates", 20,50)

class Money(Item):
    def __init__(self):
        Item.__init__(self, "Money", "A gold coin. Money can be exchanged for goods and services.", 1,1)
  
