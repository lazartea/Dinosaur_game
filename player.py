import os
from item import Item
import updater
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.item_weight = 0
        self.strength = 100
        self.money = 100
        self.health = 100
        self.alive = True
        self.win = False
        self.leveluplist = [150,200,250,300,350,450,550]
        updater.register(self)

    def goDirection(self, direction):
        if self.location.getDestination(direction) == None:
            print()
            print("Not a valid direction.")
            input("Press enter to continue...")
        else:
            self.location = self.location.getDestination(direction)  

    def update(self):
        if self.health < 50:
                self.strength -= 1
                clear()
                print()
                print("You are injured. You have lost strength.")
                print()
                input("Press enter to continue...") 
        elif self.health in self.leveluplist:
            clear()
            print()
            print("Your health is so high that you have leveled up! Your strength has increased by 10.")
            self.strength += 10
            print()
            input("Press enter to continue...")
        else:
            if random.random() > .5:
                self.health += 1
                clear()
                print("Time has passed and you have gained 1 health. You feel slightly rejuvenated.")
                print()
                input("Press enter to continue...")
            if self.win == True:
                print("You are have won the game. You are a great asset to humankind.")


    def pickup(self, item):
        #if the item will go over your strength limit, you can't pick it up
        if self.strength > item.weight + self.item_weight:
            self.items.append(item)
            item.loc = self
            self.location.removeItem(item)
            self.item_weight += item.weight
        else:
            print()
            self.health -= 10
            print('You are not strong enough to pick up this item. You strained your back trying to lift it. Your health is now '+str(self.health))
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
    def attackMonster(self, mon, weapon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
    
        if random.random() < mon.prob:
            self.health -= mon.damage
            print("The " + mon.name +" injures you.")
            print("Your health is " + str(self.health)+".")
            print("The "+ mon.name + "s health is " + str(mon.health) +".")
            if self.health <= 0:
                print("You lose.")
                self.alive = False
            
        else:
            mon.health += weapon.impact
            print("You injure the " + mon.name)
            print("Your health is " + str(self.health)+".")
            print("The "+ mon.name + "'s health is " + str(mon.health)+".")
            if mon.health <= 0:
                mon.die()
                print("You win. Your health is now " + str(self.health) + ".")
                print("You have gained 5 strength points.")
                self.strength += 5
                self.location.addLoot(self)
                if mon.name == "Angry T-Rex":
                    self.win = True 
        
        print()
        input("Press enter to continue...")

    def talkMer(self,mer):
        clear()
        print("You walk up to "+ mer.name+".")
        print()
        print(mer.name+" has the following items for sale: ")
        for item in mer.inven:
            print(item.name+": "+item.desc+" Price: "+str(mer.inven[item]))
        
        print()

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
        if item in self.items:
            self.items.remove(item)
        elif item in self.location.items:
            self.location.removeItem(item)

        self.health += item.impact

        print('Your health is now '+str(self.health))
        print()
        input("Press enter to continue...")

    def buy(self,item,mer):
        clear()
        
        
        if mer.inven[item] > self.money:
            print("You do not have enough money.")
            input("Press enter to continue...")
        elif self.item_weight + item.weight > self.strength:
            self.money -= mer.inven[item]
            self.health -= 10
            self.location.addItem(item)
            print('You are not strong enough to pick up this item. You strained your back trying to lift it. Your health is now '+str(self.health))
            input("Press enter to continue...")
        else:
            self.money -= mer.inven[item]
            self.items.append(item)
            item.loc = self
            self.item_weight += item.weight

    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i

        return False






