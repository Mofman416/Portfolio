
#This is a program made to simulate controlling the volume and channel for a television.
class Television():

    def __init__(self,name="tv",vol="5",chan="2"):
        #Hey, guess what I found out? init is short for initiate! It's the first thing that runs every
        #time you run the program!
        print("The TV: " + name + " is on!")
        self.name = name
        self.volume = vol
        self.channel = chan

    def SetVolume(self):
        #This is the function made to control the volume
        print("\nHere you can change the volume.")
        vol = input("\nSet the volume between 0-10 ")
        if int(vol) <= 10 and int(vol) >= 0:
            self.volume = vol
            print(self.volume)
            print("\nYou have successfuly set the volume!")
        else:
            print("\nIt is either out of range or not in a valid format.")

    def SetChannel(self):
        #This is the function made to control the television channel
        print("\nSet the channel from 0-99.")
        chan = input("\nGo on then! Put in a number between 0-99! ")
        if int(chan) <= 99 and int(chan) >= 0:
            self.channel = chan
            print(self.channel)
            print("\nYou've set the channel!")
        else:
            print("\nIt is either out of range or not in a valid format.")

    def ShowStatus(self):
        #This function will display current settings
        print(self.name + "- Current Volume: " + self.volume + ", Current Channel: " + self.channel + ".\n")

def main():
    #This begins the code. It's what's called to start everything.
    start = input("Press Enter to turn the TVs on.")
    user = Television("Henry")
    otherSet = Television("Chuck")
    otherSet.volume="1"
    print("\nChange the volume or channel!")
    choice = None
    while choice != "0":
        user.ShowStatus()
        otherSet.ShowStatus()
        choice = input("\nWhat would you like to do?"
                       "\nPress 1 to alter the volume (Current Volume: "+user.volume+")"
                       "\nPress 2 to alter the channel (Current Channel: "+otherSet.volume+")"
                       "\nPress 0 to quit. ")
        if choice == "0":
            print("\nBye!")
        elif choice == "1":
            user.SetVolume()
        elif choice == "2":
            user.SetChannel()
        else:
            print("\nInvalid option.")

main()