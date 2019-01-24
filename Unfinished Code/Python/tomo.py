import time

stime = time.time()

class Critter(object):
    ##A virtual pet##
    def __init__(self, name, hunger = 0, boredom = 0):
        print("A new critter has been born!")
        self.__name = name
        self.boredom = 0
        self.hunger = 0

    @property
    def name(self):
        #Get name
        return self.__name

    @name.setter
    def name(self, new_name):
        #Set Name
        if new_name == "":
            print("A critter's name can't be an empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    def talk(self):
        #Displays critter status
        print("\nHi, I'm", self.name)
        print("\nMy boredom level is", self.boredom)
        print("\nMy hunger level is", self.hunger)
        print("\nWith the two taken into consideration, I am", self.mood)
        self.pass_time

    def __pass_time(self):
        global stime
        #Passes the time for hunger and happiness
        cur_time = time.time()
        x = stime - cur_time
        self.hunger += .25*x
        self.boredom += .25*x
        stime = time.time()

    def play(self):
        #This function helps with the happiness rating.
        print("Play with your pet!")
        if self.boredom<0:
            boredom = 0
            self.__pass_time()
        else:
            self.__pass_time()

    def eat(self):
        #Feeds the pet
        print("Feed your pet!")
        if self.hunger<0:
            hunger = 0
            self.__pass_time()
        else:
            self.__pass_time()

    @property
    def mood(self):
        #Shows unhappiness
        unhappiness = int(self.boredom) + int(self.hunger)
        if unhappiness <5:
            mood = "Happy"
        elif unhappiness <=10:
            mood = "Okay"
        elif unhappiness <=15:
            mood = "Frustrated"
        else:
            mood = "Mad"
        return mood

def main():
    #This is the main function!
    critname = input("\nWhat is the name of your critter? ")
    crit = Critter(critname)
    choice = None
    while choice != "0":
        choice = input("\nWhat will you do? You can check on your critter (1), feed it (2), play with it (3), or quit (0)")
        if choice == "0":
            print("\nBye!")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("\nBad idea.")

main()

crit = Critter("Poochie")
crit.talk()

print("\nMy critter's name is:", end=" ")
print(crit.name)

print("\nAttempting to change my critter's name to Randolph.")
crit.name = "Ranolph"

#Get help with talk