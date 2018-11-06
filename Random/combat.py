#Michael
#10/12
import random

win = 0
phealth = 100
mhealth = 100
print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero uinsheathes the sword for the final battle.\n")
choice = input("Fight or Run ")

while choice.lower() == "fight":
    playerDamage = random.randrange(0,30)
    print("You attack the trolls and dealt", playerDamage, "damage killing hundreds of trolls.")
    mhealth -= playerDamage
    if mhealth > 0:
        monsterDamage = random.randrange(0, 50)
        print("The trolls fight back doing", monsterDamage, "damage.")
        phealth -= monsterDamage
    if phealth <=0:
        print("You have Died")
        win = 0
        break
    if mhealth <=0:
        print("Yay.")
        win = 1
        break
    elif phealth >=0 and mhealth >= 0:
        print("You have",phealth,"health")
        print("The Trolls have",mhealth,"health")
        choice = input("Fight or Run? ")
        if choice == "fight":
            print("You attack again.")
        elif choice == "run":
            break

if choice == "run":
    print("What a punk.")
if win == 0:
    print("Game Over")
else:
        print("You win")
