import os
from item import Item

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.item_weight = 0
        self.strength = 100
        self.money = 100
        self.health = 50
        self.alive = True
    def goDirection(self, direction):

        self.location = self.location.getDestination(direction)
    def pickup(self, item):
        #if the item will go over your strength limit, you can't pick it up
        if self.strength > item.weight + self.item_weight:
            self.items.append(item)
            item.loc = self
            self.location.removeItem(item)
            self.item_weight += item.weight
        else:
            self.health -= 10
            print()
            print('You are not strong enough to pick up this item. You strained your back trying to lift it. Your health is now '+str(self.health)))
            input("Press enter to continue...")
    def drop(self, item):
        self.items.remove(item)
        self.location.addItem(item)
        print("You have dropped " +item.name)
    def inspect(self,item):
        print(item.desc)
        input("Press enter to continue...")
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        inv_dict = {}
        #prints out the number of each item
        for i in self.items:
            if i.name not in inv_dict:
                inv_dict[i.name] = 1
            else:
                inv_dict[i.name] = inv_dict[i.name] + 1
        
        for key in inv_dict:
            if inv_dict[key] == 1:
                print(key)
            else:
                print(key+ " X" + str(inv_dict[key]))
        print("Total weight:"+str(self.item_weight))
        print()
        input("Press enter to continue...")
    def attackMonster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.health > mon.health:
            self.health -= mon.health
            if self.health < 50:
                self.strength -= 10
                print("You are injured. You have lost strength.")
            print("You win. Your health is now " + str(self.health) + ".")
            mon.die()
            self.location.addLoot(self)
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")

    def talkMer(self,char):
        clear()
        print("You walk up to "+ char.name+".")
        print()
        print(char.name+" sells "+char.kind+".")
        print(char.name + " has " + str(char.amount) + ".")
        print(char.kind + " costs " + str(char.price) + ".")

    def status(self):
        clear()
        print()
        print("health: " + str(self.health))
        print("strength: " + str(self.strength))
        print("money: " + str(self.money))
        print()
        input("Press enter to continue...")

    def eat(self, item):
        clear()
        self.items.remove(item)
        self.health += 1
        item.location = None
        print('Your health is now '+str(self.health))
        print()
        input("Press enter to continue...")

    def buy(self,amt,mer):
        clear()
        if int(amt) > mer.amount:
            print("You cannot buy that many.")
        else:
            self.money -= mer.price 
            if mer.kind == "food":
                self.health += int(amt)

            else:
                n = int(amt)
                for item in mer.itemlist:
                    while n > 0:
                        if (self.item_weight + mer.weight) <= self.strength:
                            self.items.append(item)
                            self.item_weight += mer.weight
                            mer.itemlist.remove(item)
                            n -= 1
                        else:
                            n = 0 
                            print("You cannot carry that many.")

    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False








