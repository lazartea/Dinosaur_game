import random
import updater
from room import Room

class Monster:
    def __init__(self, name, health, prob, damage):
        self.name = name
        self.health = health
        self.loc = None
        self.prob = prob #the probability that the monster will hurt player
        self.damage = damage #the damage to player's health that will occur if an attack is unsuccessful
        
        updater.register(self)

    def update(self):
        if random.random() < .5 and self.name != "Angry T-Rex": #angry T-rex is the final monster so he doesn't move
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
        Monster.__init__(self,"Angry T-Rex",125, .50, 30)

class Pterodactyl(Monster):
    def __init__(self):
        Monster.__init__(self,"Pterodactyl",40, .10, 5)

class Spinosaurus(Monster):
    def __init__(self):
        Monster.__init__(self,"Spinosaurus",60, .20, 15)
        
class Allosaurus(Monster):
    def __init__(self):
        Monster.__init__(self,"Allosaurus",75, .25, 12)
        
class Sarcosuchus(Monster):
    def __init__(self):
        Monster.__init__(self,"Sarcosuchus",50, .30, 25)
