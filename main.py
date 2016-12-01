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
    f1 = Room("You walk east past junpiers and large boulders.\nYou traipse over a small trickling creek and see a hut with a thatched roof directly to the south.\n Smoke spirals out of a clay chimney and you can hear the sounds of a grunting dinosaur inside.\nThis must be the store that your parents went to before they were murdered by the Angry T-Rex.")
    f2 = Room("You walk parallel to the stream and away from the hut and can hear pterodactyls crying from above.\nYou think of when you were a wee baby Dinosaur and when a pterodactly flew off with your baby brother.")
    f3 = Room("You are in the thatched roof hut. Inside, there is a smarmy stegosaurus who looks like he wants to sell you something. There are a wide variety of items laid out on the table.\nThe hide of a sabertooth tiger is draped over a large dinosaur-sized chair next to the fireplace.")
    f4 = Room("You walk deeper into the forest. You can no longer hear the trickle of the creek or see the smoke from the hut. The vines and undergrowth are very thick.")
    f5 = Room("The forest seems to be thinning out. The sun is making its way successfully through the canopy and you feel happy again.")
    f6 = Room("You come to the edge of the forest. Past the last of the ancient Junipers")
    bstart = Room("You see a beach in the distance.")
    b1 = Room("You are on the shore. You can head south and into the ocean to go for a swim.")
    b2 = Room("You are in the water. The turqoise ocean feels good on your scaley feet. You submerge yourself in the water and feel refreshed.\nNow where is that Angry T-Rex?!")
    b3 = Room("You are in the ocean. You look back to the shore and can see a cave to the east of the beach.\n A wall of cliffs block the way North from the beach. Maybe the Angry T-Rex is in there?\nYou are hungry for revenge.")
    cstart = Room("You are at the mouth of a cavernous cave. The darkness is impenetrable, but you are not scared. This is the only way to avenge your family.")
    c1 = Room("You are inside the cave now and you fumble around blindly knocking into the walls... it looks like there is open space to the East and to the North...")
    c2 = Room("You hit a dead end. A pile of bones in the corner weighs heavily on your mind. You look to the east and see a rock wall dripping with slime. You must turn back.")
    c3 = Room("You see something bright in the distance of the cave. Your eyes were just beginning to adjust to the darkness and you are blinded.\nYou imagine the Angry T-Rex getting lost in the same cave and your resolve to avenge your parents strenthens.")
    c4 = Room("You are still in a in a cave. The darkness is overwhelming. You accidentally crush a skull with your foot.")
    dstart = Room("You are on a volcano. You look to the west and see the mouth of the cave that you nearly got lost in. To the east a volcano towers over you.")
    d1 = Room("You are on the summit a volcano. You walk on the edge of the crater and view the pulsing lava below.")
    d2 = Room("You move to the side of the volcana slope and can see a river of molten lava.")
    d3 = Room("A waterfall of crystal clear water is cascading off of the edge of the volcano and onto a lava field, evaporating instantly upon contact.")


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
    Room.connectRooms(c4,"west",cstart,"east")
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
    Monster("Angry T-Rex", 100, d3, .5, 25)
    Monster("Pterodactyl", 100, start, .5, 25)
    inventory_dict = {}
    inventory_list = [Item("spear","A long wooden spear with a Velociraptor tooth on the end. Increases your damage during a fight.",25), Item("Dagger","A sharp blade. Increases your damage during a fight with a small dinosaur.",5), Item("Pistol","Allows you to damage dinosaurs in a fight without the risk of retaliation. Only able to be used once.",15), Item("Sword","Increases your damage during a fight.",25), Item("Anvil","Very heavy.",10000000), Item("Cigarettes","Decreases your health.",1),Item("armor","Protects you from damage during a fight. Can only be used once.",50)]
    for item in inventory_list:
        inventory_dict[item] = item.weight * 2
    Merchant("Stegosaurus", inventory_dict, f3)
   

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
                command = input("What do you want to buy? ")
                target2 = target.getItemByName(command)
                t = player.buy(target2,target)

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

    



