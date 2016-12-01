import random
import updater

class Monster:
    def __init__(self, name, health, room, prob, damage):
        self.name = name
        self.health = health
        self.room = room
        self.prob = prob
        self.damage = damage
        room.addMonster(self)
        updater.register(self)
    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())

        if self.name == "Pterodactyl":
            if random.random() < .2:
                player.health -= 10
                self.health += 10
                player.money -= 10
                print("A Pterodactyl swoops in and attacks. You lose 10 health and 10 money.")

    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    def die(self):
        self.room.removeMonster(self)
        updater.deregister(self)
