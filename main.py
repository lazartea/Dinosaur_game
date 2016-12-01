from room import Room
from player import Player
from item import Item
from monster import Monster

from Character import Merchant
import os
import updater


player = Player()

def createWorld():
    start = Room("You are in the forest. You are a dinosaur, born from a long lineage of dinosaurs.\nVines hang down to the forest floor from massive old-growth trees. You are hungry.\nYour parents were eaten by an Angry T-Rex. You are sad. You have options, however.\nYou are facing North and trees block you path forward, to the left, and behind you.\nYou can only turn right and make your way east towards your old home. \n\nLast you heard, the Angry T-Rex was headed for a Volcano on the other side of the island.\n\nType 'go east' to walk in this direction.")
    f1 = Room("You walk east east, past junpiers and large boulders. You traipse over a small trickling creek and see a stegasaurus munching on some ferns. If you would like to talk to the merchant, use the talk command, otherwise you should keep tracking down the Angry T-Rex.")
    f2 = Room("You walk deeper into the forest.")
    f3 = Room("You walk deeper into the forest.")
    f4 = Room("You walk deeper into the forest.")
    f5 = Room("The forest seems to be thinning out.")
    f6 = Room("You come to the edge of the forest.")
    bstart = Room("You see a beach in the distance.")
    b1 = Room("You are on the shore.")
    b2 = Room("You are in the water.")
    b3 = Room("You are in the water.")
    cstart = Room("You are at the mouth of a cave.")
    c1 = Room("You enter the cave.")
    c2 = Room("You hit a dead end.")
    c3 = Room("You see something bright in the distance of the cave.")
    c4 = Room("You are in a cave.")
    dstart = Room("You are on a volcano.")
    d1 = Room("You are on a volcano.")
    d2 = Room("You are on a volcano.")
    d3 = Room("You are on a volcano.")

    Room.connectRooms(start, "east", f1, "west")
    Room.connectRooms(f1, "north", f2, "south")
    Room.connectRooms(f1, "south", f3, "north")
    Room.connectRooms(f3, "east", f6, "west")
    Room.connectRooms(f6, "north", f5, "south")
    Room.connectRooms(f5, "north", f4, "south")
    Room.connectRooms(f4, "west", f2, "east")
    Room.connectRooms(f6,"east",bstart,"west")
    Room.connectRooms(bstart,"south",b2,"north")
    Room.connectRooms(b2,"east",b3,"west")
    Room.connectRooms(b3,"north",b1,"south")
    Room.connectRooms(b1,"west",bstart,"east")
    Room.connectRooms(b1,"east",cstart,"west")
    Room.connectRooms(cstart,"north",c1,"south")
    Room.connectRooms(c2,"south",c1,"north")
    Room.connectRooms(c1,"east",c3,"west")
    Room.connectRooms(c3,"south",c4,"north")
    Room.connectRooms(c4,"east",cstart,"west")
    Room.connectRooms(c4,"east",dstart,"west")
    Room.connectRooms(dstart,"east",d1,"west")
    Room.connectRooms(d1,"north",d2,"south")
    Room.connectRooms(d1,"south",d3,"north")

    listthing = [Item("Rock","This is just a rock",15) for i in range(5)]
    h = Item("Leaf", "This is just a leaf.",15)
    c = Item("Boulder","A large boulder.",150)
    for item in listthing:
        item.putInRoom(start)
    h.putInRoom(start)
    c.putInRoom(start)
    player.location = start
    Monster("Angry T-Rex", 100, start, .5, 25)
    Merchant("Argentinosaurus","food","gives you health",15,4,0,start)
    Merchant("Stegosaurus","spear","is a weapon",5,50,25,start)
    print("You wake up alone.")

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

    



