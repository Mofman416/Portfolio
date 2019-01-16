# Michael Freeman
#11/27/18

#Hero's Inventory

import os
import random

#Hud Function
def hud():
    print("stats:", player_stats)
    print("inventory:", inventory)
    print("equipped:", equipped)

#Stats and inventory
player_health = 100
player_armor = 1250
player_attack = 250
player_money = 0
inventory = ["rusty sword", "leather armor", "wood shield", "small healing potion"]
max_inventory = 10
equipped = []
player_stats = ["health", player_health, "armor", player_armor,
            "attack", player_attack, "money", player_money]
chest_items = ["Iron sword", "metal armor", "iron shield", "large healing potion", "sun", "holy hand grenade"]


#Displays what the player has
print("As you set out on your journey you have the following.\n")
print("player stats\n")
print(player_stats)
print()
print("Your items include:")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")
os.system('cls')
hud()


#Inventory space and what can be picked up
print("You have", len(inventory), "/", max_inventory, "items in your possession.")
print("So you can pick ip", (max_inventory)-len(inventory), "more items." )
print("\nPress the enter key to continue.")
os.system('cls')
hud()

#Potion tutorial
print("You get attacked and take damage")
player_stats[1] -=22
input("\nPress the enter key to continue.")
os.system('cls')
hud()


input("\nYou have taken damage on your journey. \n"+
      "your health is at " +str(player_stats[1])+"\n"+
      "you need to use your potion \n Press the enter key to continue.")

if "small healing potion" in inventory:
    print("You've used a potion. You will live to fight another day!")
    player_stats[1]+=20
    inventory.remove("small healing potion")
input("\nPress the enter key to continue.")
os.system('cls')
hud()


#Armor tutorial
for i in range(len(inventory)):
    print(str(i),inventory[i])
print("lets equip some armor")
index = int(input("\nEnter the index number for an armor item you wish to equip: "))

while index>len(inventory)-1 or index<0 and index!= "":
    print("The number is out of range.")
    index = int(input("\nEnter the index number for an armor item in inventory."))
print("you equip your ", inventory[index])
equipped.append(inventory[index])
inventory.remove(inventory[index])
if "leather armor" in equipped:
    player_stats[3] += 1000
if "wood shield" in equipped:
    player_stats[3] += 500
input("\nPress the enter key to continue.")
os.system('cls')
hud()

#Loot
chest = []
for i in range(random.randrange(len(chest_items))):
    item = random.choice(chest_items)
    chest.append(item)

print("You find a chest which contains: ")
print(chest)
print()
print("You add the contents of the chest to your inventory.")
inventory += chest
if len(inventory) + len(chest) < max_inventory:
    inventory += chest
else:
    drop = len(inventory) + len(chest) - man_inventory
    for i in range(drop):
        x=random.choice(chest)
        chest.remove(x)
    inventory += chest
input("\nPress enter to continue.")
os.system('cls')
hud()

print("convert treasure to gold")
if "gold" in inventory:
    player_stats[7]+=100
    inventory.remove("gold")
if "gems" in inventory:
    player_stats[7]+=1000
    inventory.remove("gems")
input("\nPress the enter key to continue.")
os.system('cls')
hud()

if player_stats[7] > 100:
    print("You want to trade your sword for a crossbow. So you sell your\n"+
          " sword for 20 gold and buy a crossbow for 100 gold")
    player_stats[7]+=20
    player_stats[7]-=100
    inventory[0] = "crossbow"
input("\nPress the entry key to continue.")
os.system('cls')
hud()

print("You trade in the last two items from your inventory for a new item.")
inventory[len(inventory)-2:len(inventory)] = ["orb of future telling"]
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("In a great battle, your shield was destroyed.")
for i in range(len(inventory)):
    del inventory[i]
for i in range(len(equipped)):
    if equipped[i] == "wood shield":
        del equipped[i]
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("Your first 2 items in your inventory are stolen by theives.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)
print("\nPress the enter key to continue.")
os.system('cls')


input("\nPress the enter key to continue.")
