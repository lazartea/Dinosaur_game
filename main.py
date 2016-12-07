from room import Room
from player import Player
from item import Dagger, Rock, Boulder, Stick, Armor, Pistol, Sword, Item, Leaf, Money, Cigarette
from monster import Monster, TRex, Pterodactyl, Sarcosuchus, Allosaurus, Spinosaurus
import random
from Character import Merchant
import os
import updater


player = Player()

def createWorld():
    start = Room("You are in the forest. You are a dinosaur, born from a long lineage of dinosaurs.\nVines hang down to the forest floor from massive old-growth trees. You are hungry.\nYour parents were eaten by an Angry T-Rex. You are sad. You have options, however.\nYou are facing North and trees block you path forward, to the left, and behind you.\nYou can only turn right and make your way east towards your old home. \n\nLast you heard, the Angry T-Rex was headed for a Volcano on the other side of the island.\n\nType 'help' for help.","F")
    f1 = Room("You walk east past junpiers and large boulders.\nYou traipse over a small trickling creek and see a hut with a thatched roof directly to the south.\n Smoke spirals out of a clay chimney and you can hear the sounds of a grunting dinosaur inside.\nThis must be the store that your parents went to before they were murdered by the Angry T-Rex.","F1")
    f2 = Room("You walk parallel to the stream and away from the hut and can hear pterodactyls crying from above.\nYou think of when you were a wee baby Dinosaur and when a pterodactly flew off with your baby brother.","F2")
    f3 = Room("You are in the thatched roof hut. Inside, there is a smarmy stegosaurus who looks like he wants to sell you something. There are a wide variety of items laid out on the table.\nThe hide of a sabertooth tiger is draped over a large dinosaur-sized chair next to the fireplace.","F3")
    f4 = Room("You walk deeper into the forest. You can no longer hear the trickle of the creek or see the smoke from the hut. The vines and undergrowth are very thick.","F4")
    f5 = Room("The forest seems to be thinning out. The sun is making its way successfully through the canopy and you feel happy again.","F5")
    f6 = Room("You come to the edge of the forest. Past the last of the ancient Junipers","F6")
    bstart = Room("You see a beach in the distance.","B")
    b1 = Room("You are on the shore. You can head south and into the ocean to go for a swim.","B1")
    b2 = Room("You are in the water. The turqoise ocean feels good on your scaley feet. You submerge yourself in the water and feel refreshed.\nNow where is that Angry T-Rex?!","B2")
    b3 = Room("You are in the ocean. You look back to the shore and can see a cave to the east of the beach.\n A wall of cliffs block the way North from the beach. Maybe the Angry T-Rex is in there?\nYou are hungry for revenge.","B3")
    cstart = Room("You are at the mouth of a cavernous cave. The darkness is impenetrable, but you are not scared. This is the only way to avenge your family.","C")
    c1 = Room("You are inside the cave now and you fumble around blindly knocking into the walls... it looks like there is open space to the East and to the North...","C1")
    c2 = Room("You hit a dead end. A pile of bones in the corner weighs heavily on your mind. You look to the east and see a rock wall dripping with slime. You must turn back.","C2")
    c3 = Room("You see something bright in the distance of the cave. Your eyes were just beginning to adjust to the darkness and you are blinded.\nYou imagine the Angry T-Rex getting lost in the same cave and your resolve to avenge your parents strenthens.","C3")
    c4 = Room("You are still in a in a cave. The darkness is overwhelming. You accidentally crush a skull with your foot.","C4")
    dstart = Room("You are on a volcano. You look to the west and see the mouth of the cave that you nearly got lost in. To the east a volcano towers over you.","V")
    d1 = Room("You are on the summit a volcano. You walk on the edge of the crater and view the pulsing lava below.","V1")
    d2 = Room("You move to the side of the volcano slope and can see a river of molten lava.","V2")
    d3 = Room("A waterfall of crystal clear water is cascading off of the edge of the volcano and onto a lava field, evaporating instantly upon contact.","V3")
    AllRooms = [start,f1,f2,f3,f4,f5,f6,bstart,b1,b2,b3,cstart,c1,c2,c3,c4,dstart,d1,d2,d3]

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

    rocks = [Rock() for i in range(25)]
    boulders = [Boulder() for i in range(3)]
    leaves = [Leaf() for i in range(10)]
    sticks = [Stick() for i in range(5)]
    coins = [Money() for i in range(15)]
    items = [rocks,boulders,leaves,sticks,coins]
    

    #adds rocks, sticks, coins, and leaves randomly to rooms
    for ls in items:
        for i in ls:
            i.putInRoom(random.choice(AllRooms))
    
    
    player.location = start

    p = [Pterodactyl() for i in range(8)]
    ss = [Sarcosuchus() for i in range(3)]
    s = [Spinosaurus() for i in range(2)]
    a = [Allosaurus() for i in range(5)]
    monsters = [p,ss,s,a]
    for ls in monsters:
        for m in ls:
            m.putInRoom(random.choice(AllRooms)) #monsters assigned randomly to rooms
    rex = TRex() 
    rex.putInRoom(d2) #TRex is the final monster, so he's at the end of the map
    
    inventory_dict = {}

    inventory_list = [Sword(), Dagger(), Pistol(), Armor(),Stick(),Leaf(),Cigarette()]
    
    for item in inventory_list:
        inventory_dict[item] = item.weight * 2

    merch = [Merchant(inventory_dict) for i in range(3)]
    for i in merch:
        i.putInRoom(random.choice(AllRooms)) #three merchants scattered randomly
   

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        inv_dict = {}
        #prints out the number of each monster for stacking
        for i in player.location.monsters:
            if i.name not in inv_dict:
                inv_dict[i.name] = 1
            else:
                inv_dict[i.name] = inv_dict[i.name] + 1
        
        for key in inv_dict:
            if inv_dict[key] == 1:
                print(key)
            else:
                print(key+ " X" + str(inv_dict[key]))
        print()
    if player.location.hasMer():
        print("This room contains the following merchants:")
        inv_dict = {}
        #prints out the number of each merchant for stacking
        for i in player.location.merchants:
            if i.name not in inv_dict:
                inv_dict[i.name] = 1
            else:
                inv_dict[i.name] = inv_dict[i.name] + 1
        
        for key in inv_dict:
            if inv_dict[key] == 1:
                print(key)
            else:
                print(key+ " X" + str(inv_dict[key]))
        print()
    if player.location.hasItems():
        print("This room contains the following items:")

        inv_dict = {}
        #prints out the number of each item for stacking
        for i in player.location.items:
            if i.name not in inv_dict:
                inv_dict[i.name] = 1
            else:
                inv_dict[i.name] = inv_dict[i.name] + 1
        
        for key in inv_dict:
            if inv_dict[key] == 1:
                print(key)
            else:
                print(key+ " X" + str(inv_dict[key]))


        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("attack <monster> -- attacks monster")
    print("drop <item> -- drops the item")
    print("eat <object> -- eats an item and adjusts health")
    print("exit -- ends the game")
    print("go <direction or abbreviation> -- moves you in the given direction")
    print("inspect <item> -- gives item description")
    print("inventory -- displays your inventory")
    print("map -- displays a map with your location marked")
    print("me -- displays stats")
    print("pickup <item> -- picks up the item")
    print("talk <character> -- talks to character")
    print("wait -- passes time")
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
        if len(commandWords) > 0: #fixes error where game crashes if you press enter without a command
            
            if commandWords[0].lower() == "go":   #cannot handle multi-word directions
                if len(commandWords) > 1: #bug fix if only 'go' is entered
                    if commandWords[1][0].lower() == 's': #allows for abbreviations
                        player.goDirection("south") 
                        timePasses = True 
                    elif commandWords[1][0].lower() == 'n':
                        player.goDirection("north") 
                        timePasses = True
                    elif commandWords[1][0].lower() == 'w':
                        player.goDirection("west") 
                        timePasses = True
                    elif commandWords[1][0].lower() == 'e':
                        player.goDirection("east") 
                        timePasses = True
                    else:
                        player.goDirection(commandWords[1]) 
                        timePasses = True
                else:
                    print("Not a valid direction.")
                    commandSuccess = False
            elif commandWords[0].lower() == "wait": #time passes
                timePasses = True
            elif commandWords[0].lower() == "inspect": #inspects item
                targetName = command[8:]
                target = player.location.getItemByName(targetName)
                if target != False:
                    player.inspect(target)
                else:
                    print("No such item.")
                    commandSuccess = False
            elif commandWords[0].lower() == "map": #prints a map to the terminal with the player's location
                clear()
                file_object = open("map.txt","r")
                print()
                print(file_object.read())
                print()
                print("You are in " + player.location.number + ".")
                print()
                file_object.close()
                timePasses = True
                input("Press enter to continue...")

            elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
                targetName = command[7:]
                target = player.location.getItemByName(targetName)
                if target != False:
                    if targetName.lower() == "money": #money isn't added to your inventory
                        player.money += 1
                        player.location.items.remove(target) #once it is used, it disappears
                    else:
                        player.pickup(target)
                else:
                    print("No such item.")
                    commandSuccess = False

            elif commandWords[0].lower() == "drop":  #drops the specified item
                targetName = command[5:]
                target = player.getItemByName(targetName)
                if target != False:
                    player.drop(target)
                else:
                    print("No such item.")
                    commandSuccess = False
            elif commandWords[0].lower() == "inventory": #shows the player's inventory
                player.showInventory()        
            elif commandWords[0].lower() == "help": #lists commands
                showHelp()
            elif commandWords[0].lower() == "exit": #ends the game
                playing = False
   
            elif commandWords[0].lower() == "attack": #attacks the specified monster
                targetName = command[7:]
                target = player.location.getMonsterByName(targetName)
                steg = player.location.getMerByName(targetName) #checks to see if you're trying to kill a merchant
                if target != False:
                    command = input("Which weapon? ")
                    target2 = player.getItemByName(command)
                    
                    if target2 != False:
                        player.attackMonster(target,target2)
                        while target.health > 0 and player.health > 0:
                            command2 = input("Attack again? y/n \n")
                            if command2 == 'y':
                                player.attackMonster(target,target2)
                            elif command2 == 'n':
                                 print("You ran away! Your parents would be ashamed.")
                                 input("Press enter to continue...")
                                 break
                            else:
                                print("Not a command. Please type y or n!")
                                input("Attack again? y/n")     
                    elif target2 == False:
                        print("Not a valid weapon.")
                        input("Press enter to continue...")
                    else:
                        input("Press enter to continue...")
                elif steg != False:
                    clear()
                    print("Stegosaurus is your friend!")
                    print("He is so offended that you attempted to attack him that he rallies a group of merchants to defeat you.")
                    print("They come when you are least expecting it, and they kill you in your sleep.")
                    print("You lose.")
                    input("Press enter to die...")
                    playing = False #other lose condition
                else:
                    print("No such monster.")
                    commandSuccess = False
            elif commandWords[0].lower() == "eat": #eats an item (can lower your health if it's a nonfood item)
                targetName = command[4:]
                print(targetName)
                target = player.getItemByName(targetName)
                target2 = player.location.getItemByName(targetName)
                if target != False:
                    player.eat(target)
                elif target2 != False:
                    player.eat(target2)
                else:
                    print (targetName)
                    print("No such item.")
                    commandSuccess = False


            elif commandWords[0].lower() == "talk": #talks to a character
                targetName = command[5:]
                target = player.location.getMerByName(targetName)
                if target != False:
                    player.talkMer(target)
                    command = input("What do you want to buy? ")
                    target2 = target.getItemByName(command.lower())
                    if target2 != False:
                        t = player.buy(target2,target)

                else:
                    print("No such merchant.")
                    commandSuccess = False

            elif commandWords[0].lower() == "me": #lists stats
                player.status()

            
            else:
                print("Not a valid command")
                commandSuccess = False
        else:

            print("Not a valid command")
            commandSuccess = False

    if timePasses == True:
        updater.updateAll()

    



