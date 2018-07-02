# Dinosaur Game

A text-based adventure game created for Math 121. Built by Garrett Linck and Amy Rose Lazarte off of Starter code written by Adam Groce. 

Amy Rose and Garrett worked together in person throughout the majority this assignment. We used a github repository (https://github.com/lazartea/Dinosaur_game) to make our updates and additions as seamless as possible. This helped us collaborate seemlessly even when we could not meet up in person. This way, we could both be testing new implementations, flag errors, and request the addition of new features all in real time.

After Garrett's original partner dropped the class, Amy Rose joined him and began working on the plot that he had already began developing. Unfortunately, Garrett had pneumonia for the week before the first check in, so Amy Rose did the bulk of the initial coding. After his recovery, we began working together on debugging the code Amy Rose had written and implementing new features. Garrett drew the `map.txt` file based on the rooms that Amy Rose sketched out in the beginning of the project. 

Images in the `victory_screen.txt` and `lose_condition.txt` are taken from http://www.asciiworld.com/-Dinosaurs-.html

## Files
- `monster.py`
- `player.py`
- `main.py`
- `character.py`
- `room.py`
- `updater.py`
- `map.txt.` The map image.
- `victory_screen.txt` The Victory condition image.
- `lose_condition.txt` The lose condition image.


## Improvements
- drop command
  - This command was modeled after the pickup command.
- wait command 
  - The wait command causes time to pass. The player doesn't move, but random events can occur, characters/monsters move, and health can be regenerated. Time passing can also cause a wounded player to lose health, or a player with a very high level of health to gain strength.  
- random events
  - At random intervals, a Pterodactyl swoops into the current room and injures the player if they are not wearing armor. 
- me command/player attributes
  - This prints out all of the player's stats: health, strength (the amount of weight they are able to carry), and current amount of money. It will also display a message if the player is currently wearing armor. 
- inspect command 
  - This command shows the description of an item in the player's current room.
- stacking items 
  - If multiple items are in an inventory, the inventory will show the name of the item and the amount present. This will also occur if multiple items are in a room.
- loot
  - Upon successfully killing a monster, the player receives a randomly generated number of coins. A random item also appears in the current room (either a weapon or food item).
- inventory maximum size 
  - The player starts out with a certain level of strength. Each item has a weight. The total weights of all items in the inventory cannot be more than the player's strength. Attempting to pick up an item that is too heavy injures the player. Strength is gained (and therefore inventory size) when a player beats a monster or levels up by hitting a high level of health. 
- healing items 
  - Eating a leaf allows you to gain one health point. However, eating non-food items (like weapons or cigarettes) will decrease your health by different degrees. Leaves are scattered out the game randomly, and they can also be acquired as loot after defeating a monster.
- regeneration 
  - The player's health is regenerated as time passes. However, this does not occur when a player is injured. If a player's health drops below 50, time will cause health to decrease further. 
- armor 
  - Armor is an object and also an attribute. If the player picks up or buys armor, they cannot lose health during a fight. However, health can still be lost by eating non-food objects or overexertion. 
- more monsters 
  - There are five different kinds of dinosaurs with different levels of power. The final boss, Angry T-Rex, has the highest initial health, the highest probability of landing attacks, and the largest damage. Defeating this dinosaur will result in winning the game. The other dinosaurs have a range of health values, probabilities, and damages. They are not meant to be as hard to beat, and there are multiple of each type throughout the game.
- weapons 
  - There are five different types of weapons. Each weapon has a name, a description, a weight, and an impact. The level of the impact is stronger for the weapons that you have to buy (pistol, sword) than the ones that you can find throughout the rooms (sticks, rocks). Some weapons (dagger) can also be picked up as loot after defeating a monster. You cannot attack a monster without a weapon.
- currency 
  - The player starts off with an amount of money. Money is scattered randomly throughout the rooms and can also be collected after defeating a monster. Money is required to buy items from the Stegosaurus.
- bigger world 
  - The world is composed of 19 different rooms. Each room is a different area in the player's journey (forest, beach, cave, volcano). The final monster, Angry T-Rex, is located at the very end in the volcano rooms.
- map
  - The `map.txt` file contains an image of the world. When the map command is input, the file is read and printed to the screen along with the player's current location.
- victory condition
  - Upon defeating the Angry T-Rex, the player wins the game. The `victory_condition.txt` file is read and printed to the screen, and the game is ended.




