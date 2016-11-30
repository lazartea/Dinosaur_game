import random
import updater

class Monster:
    def __init__(self, name, health, room):
        self.name = name
        self.health = health
        self.room = room
        room.addMonster(self)
        updater.register(self)
    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())
    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    def die(self):
        self.room.removeMonster(self)
        updater.deregister(self)

class Velociraptor(Monster):
    name = 'Velociraptor'
    health = '75hp'
    def __init__(self):
        Monster.__init__(self)
    
class Argentinosaurus(Monster):
    name = 'Argentinosaurus'
    health = '200hp'
    
    def __init__(self):
        Monster.__init__(self)
    
class Stegosaurus(Monster):
    health = '150hp'
    name = 'Stegosaurus'
    def __init__(self):
        Monster.__init__(self)
