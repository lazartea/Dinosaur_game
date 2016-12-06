import random
import updater
from room import Room

class Monster:
    def __init__(self, name, health, prob, damage):
        self.name = name
        self.health = health
        self.loc = None
        self.prob = prob
        self.damage = damage
        
        updater.register(self)
    def update(self):
        if random.random() < .5 and self.name != "Angry T-Rex":
            room = self.loc.randomNeighbor()
            self.moveTo(room)


    def putInRoom(self, room):
        self.loc = room
        self.loc.addMonster(self)

    def moveTo(self, room):
        self.loc.removeMonster(self)
        self.loc = room
        self.loc.addMonster(self)
    def die(self):
        self.loc.removeMonster(self)
        updater.deregister(self)

class TRex(Monster):
    def __init__(self):
        Monster.__init__(self,"Angry T-Rex",500, .75, 20)

class Pterodactyl(Monster):
    def __init__(self):
        Monster.__init__(self,"Pterodactyl",100, .25, 10)

class Spinosaurus(Monster):
    def __init__(self):
        Monster.__init__(self,"Spinosaurus",200, .90, 5)
        
class Allosaurus(Monster):
    def __init__(self):
        Monster.__init__(self,"Allosaurus",150, .80, 15)
        
class Sarcosuchus(Monster):
    def __init__(self):
        Monster.__init__(self,"Sarcosuchus",115, .60, 15)
