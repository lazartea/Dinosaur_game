from room import Room
from player import Player
from item import Item
from monster import Monster
from Character import Merchant
import os
import updater


player = Player()

def createWorld():
    a = Room("You are in the forest.")
    b = Room("You are by the beach.")
    c = Room("You are in a cave.")
    d = Room("You are on a volcano.")
    Room.connectRooms(a, "east", b, "west")
    Room.connectRooms(c, "east", d, "west")
    Room.connectRooms(a, "north", c, "south")
    Room.connectRooms(b, "north", d, "south")
    listthing = [Item("Rock","This is just a rock",15) for i in range(5)]
    h = Item("Leaf", "This is just a leaf.",15)
    c = Item("Boulder","A large boulder.",150)
    for item in listthing:
        item.putInRoom(b)
    h.putInRoom(b)
    c.putInRoom(b)
    player.location = a
    Monster("Angry T-Rex", 20, b)
    Merchant("Argentinosaurus","food","gives you health",15,4,0,b)
    Merchant("Stegosaurus","spear","is a weapon",5,50,25,b)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasMer():
        print("This room contains the following merchants:")
        for c in player.location.merchants:
            print(c.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("talk <character> -- talks to character")
    print("buy <item> -- buys the item")
    print("attack <monster> -- attacks monster")
    print("me -- lists stats")
    print()
    input("Press enter to continue...")



createWorld()
playing = True
while playing and player.alive:
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()
        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            player.goDirection(commandWords[1]) 
            timePasses = True
        elif commandWords[0].lower() == "wait": 
            timePasses = True
        elif commandWords[0].lower() == "inspect":
            targetName = command[8:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.inspect(target)
            else:
                print("No such item.")
                commandSuccess = False

        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.pickup(target)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "drop":  
            targetName = command[5:]
            target = player.getItemByName(targetName)
            if target != False:
                player.drop(target)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "inventory":
            player.showInventory()        
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "exit":
            playing = False
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
            else:
                print("No such monster.")
                commandSuccess = False
        elif commandWords[0].lower() == "eat":
            targetName = command[4:]
            target = player.getItemByName(targetName)
            if target != True:
                player.eat(target)
            else:
                print (targetName)
                print("No such item.")
                commandSuccess = False


        elif commandWords[0].lower() == "talk":
            targetName = command[5:]
            target = player.location.getMerByName(targetName)
            if target != False:
                player.talkMer(target)
                command = input("How many? ")
                t = player.buy(command,target)

            else:
                print("No such merchant.")
                commandSuccess = False

        elif commandWords[0].lower() == "me":
            player.status()

        else:
            print("Not a valid command")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()

    


