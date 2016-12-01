import random
import updater
from item import Item 

class Merchant:
    def __init__(self, name, inven, room):
        self.name = name
        self.room = room
        self.inven = inven
        room.addMer(self)
        updater.register(self)


    def update(self):
        return
    
    def getItemByName(self, name):
        for i in self.inven:
            if i.name.lower() == name.lower():
                return i
        return False
            
    def moveTo(self, room):
        self.room.removeMer(self)
        self.room = room
        room.addMer(self)
    def die(self):
        self.room.removeMer(self)
        updater.deregister(self)
