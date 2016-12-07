import random
import updater
from item import Item 

class Merchant:
    def __init__(self, inven):
        self.name = "Stegosaurus"
        self.room = None
        self.inven = inven
        
        

    def getItemByName(self, name):
        for i in self.inven:
            if i.name.lower() == name.lower():
                return i
        return False
            
    def putInRoom(self, room): #merchants do not move once they are placed
        self.loc = room
        self.loc.addMer(self)

