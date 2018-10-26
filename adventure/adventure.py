#The Great Adventure

import random
import time
import sys
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
        while True:
            choice = input("Will " + name + " go left (Chapel) or right (Factory)? ")
            print()
            if choice.lower().startswith("c"):
                chapel(name)
                print("Now " + name + " is outside of the Chapel. They can still go into the factory.")
                print()
                while True:
                    choice = input("Go to the Factory (Factory) or go Home (Home)? ")
                    if choice.lower().startswith("f"):
                        factory(name)
                        end(name)
                    elif choice.lower().startswith("h"):
                        print(name, "goes home. ")
                        gameover()
                        break
                    else:
                        print("Invalid Response. Try Again.")
                        print()
            elif choice.lower().startswith("f"):
                factory(name)
                print("Now " + name + " is outside of the Factory. They can still go into the chapel.")
                print()
                while True:
                    choice = input("Go to the Chapel (Chapel) or go Home (Home)? ")
                    if choice.lower().startswith("c"):
                        chapel(name)
                        end(name)
                        break
                    elif choice.lower().startswith("h"):
                        print(name, "goes home. ")
                        gameover()
                        break
                    else:
                        print("Invalid Response. Try Again.")
            else:
                print("Invalid Response. Try again.")
                print()
            
        
        
    
    
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
            print("COMBAT RESOLVED!")
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
            else:
                print("Invalid Response. Try Again.")
    
    if action.lower().startswith("r"):
        print("You run from " + monster + ".")
        print()
        
def gameover():
    while True:
        answer = input("Do you want to restart (Restart) or Quit (Quit)? ").lower()
        print()
        if answer.startswith("r"):
            adventure()
        elif answer.startswith("q"):
            print("Thank you for playing! Have a good day!")
            kill()
            break
            
        else:
            print("Quit messing around, punk.")
            print()
        
def chapel(name):
    print(name, "walks into the old chapel.")
    print()
    print("The floors are creaky and the pews are skewed.")
    print()
    print("Suddenly, a bat appears!")
    print()
    monster = "Bat"
    monsterdamage = random.randrange(0,20)
    mhealth = 20
    monsterimage = """
                      -------------    *        *      -------------
                      \___         \  * *      * *    /         ___/
                       \____         *%%%*    *%%%*          _____/
                        \___________*%%%%%****%%%%%*_____________/
                                    *     . .      *
                                    *      W       *
                                    ****************"""
    combat(monsterdamage, mhealth, monster, phealth, poriginal, playerdamage, monsterimage, name)
    print(name, "continues inside and sees a cirlce drawn on the ground. On certain points has a lit candle except for one.")
    print()
    while True:
        choice = input("Will you light the last candle (Light) or leave (Home)? ")
        if choice.lower().startswith("l"):
            print("The candle is lit.")
            print()
            print("The ground shakes, the world darkens...")
            print()
            print("A wraith emerges and goes for you!!")
            print()
            monster = "Wraith"
            monsterimage = """
                                *******
                                *%%%%%*
                                *%%%%%*
                                *******
                                   *
                                ******
                                   *
                                   *
                                   *
                                  * *
                                 *   *"""
            monsterdamage = random.randrange(0,20)
            mhealth = 60
            combat(monsterdamage, mhealth, monster, phealth, poriginal, playerdamage, monsterimage, name)
            print("The Wraith disappears and " + name + " finds a bookshelf.")
            print()
            print("They begin reading.")
            print()
            print("'Our town is gorgeous. We thank the forces that created the land and all that it has provided us with. We use the land as a means for nourishment and giving thanks.'")
            print()
            choice = input("Continue reading (Y/N)? ")
            while True:
                if choice.upper() == "Y":
                    print("'The town began to decay. We're not sure what happened but people began dying off at a faster rate than usual.'")
                    print()
                    choice = input("Continue reading (Y/N)? ")
                    print()
                    if choice.upper() == "Y":
                        print("'As if things couldn't get worse, the food became poisoned and unfit for consumption. We're running low on options.'")
                        print()
                        choice = input("Continue reading (Y/N)? ")
                        if choice.upper() == "Y":
                            print("'Things are just horrible. People have resorted to eating each other. It's a truly nauseating thing. I am ashamed to admit that I have fallen to this activity. At first people only began eating the dead. Now they hunt each other like animals.'")
                            print()
                            choice = input("Continue reading (Y/N)? ")
                            if choice.upper() == "Y":
                                print("'It's awful. The remaining saints and I have decided to summon the forces for their aid. Something very evil came. I can hear my friends being slaughtered as I write this. It won't be long before-'")
                                print()
                                print("The record ends there.")
                                print()
                                break
                
                                
                elif choice.upper() == "N":
                    print(name, "replaces the book and leaves. That's enough adventuring for one day.")
                    print()
                    gameover()
                    break
                else:
                    print("Invalid Response. Try Again.")
            break
                
        elif choice.lower().startswith("l"):
            print(name, "left the chapel and went home.")
            print()
            gameover()
            break
        else:
            print("Invalid Choice. Try Again.")

def factory(name):
    print(name, "walks into an old factory.")
    print()
    print("The pipes hang low and metal grates act like walkways.")
    print()
    print("The smell of unused chemicals and dead things flood the area.")
    print()
    print("Out of the dark, a rat appears!")
    print()
    monster = "Rat"
    monsterdamage = random.randrange(0,20)
    mhealth = 35
    monsterimage = """
                             _______      ________
                            /       \    /        \
                            |       |    |        |
                            \        ----         /
                             |                   |
                             |    **       **    |
                             |    **       **    |
                             |         %%        |
                             \         %%        /
                              -------------------"""
    combat(monsterdamage, mhealth, monster, phealth, poriginal, playerdamage, monsterimage, name)
    print(name, "proceeded to navigate the area.")
    print()
    print("You finally reach a large pool of water in a room of the factory.")
    print()
    print("There's a button on a console from accross the room.")
    print()
    print("It looks like it'll go something with the pool.")
    print()
    while True:
        choice = input("Will you push the button (Button) or go home (Home)? ")
        print()
        if choice.lower().startswith("b"):
            print(name, "pushes the button.")
            print()
            print("The water beings to stir and makes a big whirlpool.")
            print()
            print("You can feel a rumbling...")
            print()
            print("A Kraken appears!")
            monster = "Kraken"
            monsterdamage = random.randrange(0,20)
            mhealth = 70
            monsterimage = """      ^
                                   / \
                                  /   \
                               ----------
                              |          |
                              |  []  []  |
                              |          |
                              |     0    |
                              ------------
                              ____________"""
            combat(monsterdamage, mhealth, monster, phealth, poriginal, playerdamage, monsterimage, name)
            print("A falling tentacle hits the computer and boots up a log.")
            print()
            print("With the chaos over " + name + " goes over to read the reports.")
            print()
            print(name, "begins reading the reports.")
            print("'Log 4 - We have been happily partnered with the town down river. We're working with them to see what needs to be done and what we can do to help them have a better life.'")
            print()
            choice = input("Continue Reading (Y/N)? ")
            print()
            while True:
                if choice.lower().startswith("y"):
                    print("'Log 7 - There was a big accident. We're not sure how it could affect the area, but we decided to keep it a secret to not induce mass hyteria.'")
                    print()
                    choice = input("Continue Reading (Y/N)? ")
                    print()
                    if choice.lower().startswith("y"):
                        print("'Log 12 - A rogue employee went and dumped a bunch of hallucinages and pollutants into the river before jumping in himself. He's dead. We will be if we don't fix this soon.'")
                        print()
                        choice = input("Continue Reading (Y/N)? ")
                        print()
                        if choice.lower().startswith("y"):
                            print("'Log 13 - A huge and horrible monster has been created from the radiation and pollution. It has wrecked the place. This report will continue. Stay tuned.'")
                            print()
                            print("The reports do not continue.")
                            print()
                            print(name, "shuts the machine off and leaves.")
                            print()
                            break
                elif choice.lower().startswith("n"):
                    print(name, "goes home. No more adventures.")
                    gameover()
                    break
                else:
                    print("Invalid Response. Try Again.")
            break
        elif choice.lower().startswith("h"):
            print(name,  "goes home. That's enough adventuring.")
            gameover()
            break
        else:
            print("Invalid Response. Try Again.")
            print()

def end(name):
    print(name, "begins to piece together the story.")
    print()
    print("The town and factory were once living hand in hand with each other.")
    print()
    print("Then something bad happened in the factory that affected the town.")
    print()
    print("While the factory was trying to deal with it, the town fell to cannibalism.")
    print()
    print("And then somewhere along the line the Kraken and the Wraith destroyed both places.")
    print()
    print("And now " + " has removed all the threats of the area.")
    print()
    print("The souls lost can now rest in peace.")
    while True:
        choice = input("Should anyone be told (Y/N)? ")
        if choice.lower().startswith("y"):
            print(name, "drives home and alerts the authorities.")
            print()
            print("Apparently nobody knew the town even existed.")
            print()
            print("They congratulate " + name + " for removing the threats with only a baseball bat and question them on why they were there.")
            print()
            print(name, "is sent home. They have saved many people from possible harm of the town and the creatures inside.")
            print()
            print(name, "puts the bat away and sleeps in their bed, eager for the next adventure.")
            print()
            print("Congratulations! You win!")
            print()
            gameover()
            break
        elif choice.lower().startswith("n"):
            print(name, "drives home and goes to bed.")
            print()
            print("Telling the events that have happened would snap a normal person.")
            print()
            print(name, "goes to sleep, feeling exhausted after the adventure.")
            print()
            print("Congratulations, You win!")
            print()
            gameover()
            break
        else:
            print("Invalid Responce. Please Try again.")
            print()

def kill():
    time.sleep(10)
    exit()

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


            
    
    
