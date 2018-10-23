#The Great Adventure

import random
phealth = 100
poriginal = 100
playerdamage = random.randrange(0,30)

def adventure():
    print(name + ", on their most recent adventure, finds themselves in an empty town with weeds growing over the houses. Armed with only a baseball bat they are ready for a new adventure.")
    print()
    while True:
        choice = input("Now, the first choice. Should the adventurer explore the houses (Go), or leave town (Leave) ")
        print()
        if choice.lower().startswith("g"):
            tut(name)
            
        elif choice.lower().startswith("l"):
            print(name, "goes home. Maybe they left the oven on?")
            print()
            gameover()
            break
            
        else:
            break
            print("Invalid response. Try again.")
            print()

def tut(name):
        print(name, "decides to explore some of the houses. While they are covered in weeds the structures themselves appear to have looked charred and degraded over the years.")
        print()
        print(name, "hears a rustling in the bushes...a wolf jumps out!")
        print()
        monster = "Wolf"
        mhealth = 45
        monsterdamage = random.randrange(0,20)
        monsterimage = """
                            *     *
                           * *   * *
                           * ***** *
                           * .   . *
                           *   .   *
                           *   @   *
                           *  \_/  *
                           *********"""
        combat(monsterdamage, mhealth, monster, phealth, poriginal, playerdamage, monsterimage, name)
        print(name + "'s battle took them to a new part of town.")
        print()
        print("To your left is a huge building made of wood, and to your right is a large factory.")
        choice = input("Will", name, "go left (Chapel) or right (Factory)? ")
        if choice.lower().startswith("c"):
            chapel()
        
        
        
    
    
def combat(monsterdamage, mhealth, monster, phealth, poriginal, playerdamage, monsterimage, name):
    print("COMBAT ENGAGED!")
    print()
    print(monsterimage)
    print()
    print(monster, "is attacking!")
    print()
    action = input("What are you going to do? Fight (Fight) or Flee (Run)? ")
    print()
    while action.lower().startswith("f"):
        monsterdamage = random.randrange(0,60)
        playerdamage = random.randrange(0,30)
        print("You attack", monster, "dealing", playerdamage, "in damage.")
        print()
        mhealth -= playerdamage
        if mhealth > 0:
            print(monster, "fights back, dealing", monsterdamage, "in damage!")
            print()
            phealth -= monsterdamage
        if phealth <= 0:
            print(name, "has fallen...")
            gameover()
            break
        if mhealth <= 0:
            print("You have defeated", monster, "and your health has been restored!")
            print()
            phealth = 100
            break
        elif phealth > 0 and mhealth > 0:
            print("Your health is", phealth, "/", poriginal)
            print()
            action = input("Do you continue fighting (Fight) or do you run (Run)?")
            print()
            if action.lower().startswith("f"):
                print("You attack again.")
                print()
            elif action.lower().startswith("r"):
                break
    
    if action.lower().startswith("r"):
        print("You run from " + monster + ".")
        print()
        
def gameover():
    answer = input("Do you want to restart (Restart) or Quit (Quit)? ").lower()
    print()
    if answer.startswith("r"):
        adventure()
    elif answer.startswith("q"):
        print("Thank you for playing! Have a good day!")
    else:
        print("Quit messing around, punk.")
        print()
        gameover()

print("Welcome to the Great Adventure!")
print()
print("To play this game, read the scenarios and pick an option. Options are labeled with a key word in parentheses that help with progression.")
print()
print("For example, you could choose to travel on foot (Walk) or by vehicle (Car). To progress, either type either the full word of one of the choices or the first letter of that word.")
print()
print("Now then...")
name = input("What is the name of your chracter? ")
print()
adventure()


            
    
    
