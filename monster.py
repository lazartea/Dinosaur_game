import random
import updater

class Monster:
    def __init__(self, name, health, prob, damage):
        self.name = name
        self.health = health
        self.loc = None
        self.prob = prob
        self.damage = damage
        
        updater.register(self)
    def update(self):
        if random.random() < .5:
            self.moveTo(self.loc.randomNeighbor())

        if self.name == "Pterodactyl":
            if random.random() < .2:
                player.health -= 10
                self.health += 10
                player.money -= 10
                print("A Pterodactyl swoops in and attacks. You lose 10 health and 10 money.")

    def putInRoom(self, room):
        self.loc = room
        room.addMonster(self)

    def moveTo(self, loc):
        self.loc.removeMonster(self)
        self.loc = room
        loc.addMonster(self)
    def die(self):
        self.room.removeMonster(self)
        updater.deregister(self)

class TRex(Monster):
    def __init__(self):
        Monster.__init__(self,"Angry T-Rex",500, .75, 20)

class Pterodactyl(Monster):
    def __init__(self):
        Monster.__init__(self,"Pterodactyl",100, .25, 10)
