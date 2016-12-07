import os
from item import Item, Leaf, Rock, Dagger
import updater
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.item_weight = 0 #total weight carrying. cannot be more than strength
        self.strength = 100 #inventory max
        self.money = 100
        self.health = 100
        self.alive = True 
        self.win = False 
        self.armor = False 
        self.leveluplist = [150,200,250,300,350,450,550] #strength will increase when each of these levels are reached
        updater.register(self)

    def goDirection(self, direction):
        if self.location.getDestination(direction) == None:
            print()
            print("Not a valid direction.")
            input("Press enter to continue...")
        else:
            self.location = self.location.getDestination(direction)  

    def update(self):
        #armor condition
        if self.getItemByName("Armor") != False:
            self.armor = True 

        #win condition:
        if self.win == True:
            clear()
            print("You are have won the game. You are a great asset to dinosaurkind.")
            file_object = open("victory_screen.txt","r")
            print()
            print(file_object.read())
            print()
            file_object.close()
            input("Press enter to continue...")
            exit()

        #lose condition:
        if self.health <= 0:
            self.alive = False

        if self.alive == False:
            clear()
            print()
            print("Your health has reached an unrecoverable level. You die.")
            file_object = open("lose_condition.txt","r")
            print()
            print(file_object.read())
            print()
            file_object.close()
            input("Press enter to continue...")
            print()
            exit()

        #injured condition:
        if self.health < 50:
            if self.armor == False: #armor protects you from injury
                self.strength -= 1
                clear()
                print()
                print("You are injured. You have lost strength.")
                print()
                input("Press enter to continue...") 

        #levelup condition:
        elif self.health in self.leveluplist:
            clear()
            print()
            print("Your health is so high that you have leveled up! Your strength has increased by 10.")
            self.strength += 10
            print()
            input("Press enter to continue...")

        else:

            if random.random() < .15:
                self.health += 5
                clear()
                print("Time has passed and you have gained 5 health. You feel slightly rejuvenated.")
                print()
                input("Press enter to continue...")
            else:
            #random events (in an else because you can't gain health and lose it on the same turn)
                if random.random() < .1:
                    print("A Pterodactyl swoops in and attacks. You lose 10 health.")
                    self.health -= 10
                    input("Press enter to continue...")
                    self.update()
            


    def pickup(self, item):
        #if the item will go over your strength limit, you can't pick it up
        if self.strength > item.weight + self.item_weight:
            self.items.append(item)
            item.loc = self
            self.location.removeItem(item)
            self.item_weight += item.weight
            self.update()
        else:
            print()
            self.health -= 10
            print('You are not strong enough to pick up this item. You strained your back trying to lift it. Your health is now '+str(self.health))
            input("Press enter to continue...")

    def drop(self, item):
        self.items.remove(item)
        self.location.addItem(item)
        self.item_weight -= item.weight
        print("You have dropped " +item.name)

    def inspect(self,item):
        print(item.desc)
        input("Press enter to continue...")

    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        inv_dict = {}
        #prints out the number of each item for stacking
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
            if self.armor != True: #you cannot be hurt when you are wearing armor
                self.health -= mon.damage
                print("The " + mon.name +" injures you.")
                print("Your health is " + str(self.health)+".")
                print("The "+ mon.name + "s health is " + str(mon.health) +".")
                if self.health <= 0:
                    print("You lose. You are dead. You met the same sorry fate as your parents.")
                    self.alive = False #ends game
            else:
                print("The " + mon.name +" tries to attack you. Your armor protects you.")
                input("Press enter to continue...")
            
        else:
            mon.health += weapon.impact
            
            if mon.health <= 0:
                mon.die()
                if mon.name == "Angry T-Rex": 
                    self.win = True  #victory condition
                    self.update()
                else:
                    print("You kill the " + mon.name +". Your health is now " + str(self.health) + ".")
                    print("You have gained 5 strength points.")
                    self.strength += 5
                    self.location.addLoot(self)
                    scavange = random.choice([Leaf(),Dagger(),Leaf(),Leaf(),Leaf(),Leaf()])
                    self.location.addItem(scavange) #causes loot item to enter the room
                    print("The "+mon.name+" drops a "+scavange.name+".")

                
            else:
                print("You injure the " + mon.name)
                print("Your health is " + str(self.health)+".")
                print("The "+ mon.name + "'s health is " + str(mon.health)+".")
        
        print()
        input("Press enter to continue...")

    def talkMer(self,mer):
        clear()
        print("You walk up to "+ mer.name+".")
        print()
        print(mer.name+" has the following items for sale: ")
        inv_dict = {}

        
        for item in mer.inven:
            print(item.name+": "+item.desc+" Price: "+str(mer.inven[item]))
        
        print()

    def status(self):
        clear()
        print()
        print("health: " + str(self.health))
        print("strength: " + str(self.strength))
        print("money: " + str(self.money))
        if self.armor != False:
            print("You are wearing armor.")
        print()
        input("Press enter to continue...")
        
    def eat(self, item):
        clear()
        if item in self.items: #eats item from your inventory first
            self.items.remove(item)
        elif item in self.location.items: #otherwise eats item from the room
            self.location.removeItem(item)

        self.health += item.impact #health will increase or decrease based on the item's pos/neg impact
        if self.health <= 0:
            self.alive = False
            self.update()

        print('Your health is now '+str(self.health))
        print()
        input("Press enter to continue...")

    def buy(self,item,mer):
        clear()
        
        
        if mer.inven[item] > self.money: #must have enough money
            print("You do not have enough money.")
            input("Press enter to continue...")
        elif self.item_weight + item.weight > self.strength: #must have enough strength
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






