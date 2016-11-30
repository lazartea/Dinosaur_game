import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, weight, damage):
        self.name = name
        self.desc = desc
        self.weight = weight
        self.damage = damage
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
    name = 'Pistol'
    desc = 'A .357 Magnum Revolver'
    weight = '2lb'
    damage = '50hp'
    def __init__(self):
        Item.__init__(self)
    def 

class Sword(Item):
    name = 'Sword'
    desc = 'A long steel broadsword'
    weight = '10lb'
    damage = '40hp'
    def __init__(self):
        Item.__init__(self)
        
class Dagger(Item):
    name = 'Dagger'
    desc = 'A short dagger with emeralds embedded in the hilt'
    weight = '1lb'
    damage = '15hp'
    def __init__(self):
        Item.__init__(self)
        
class Stick(Item):
    name = 'Stick'
    desc = 'A long branch from an oak tree. It's just a stick'
    weight = '2lb'
    damage = '10hp'
    def __init__(self):
        Item.__init__(self)
  
