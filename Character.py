import random
import updater

class Merchant:
    def __init__(self, name, kind, desc, price, amount, weight, room):
        self.name = name
        self.kind = kind
        self.room = room
        self.price = price
        self.desc = desc
        self.amount = amount 
        self.weight = weight
        room.addMer(self)
        updater.register(self)

    def sell(self,num):
        self.amount -= num

    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())
            self.amount -= 1
        else:
            self.amount += 1
    def moveTo(self, room):
        self.room.removeMer(self)
        self.room = room
        room.addMer(self)
    def die(self):
        self.room.removeMer(self)
        updater.deregister(self)
