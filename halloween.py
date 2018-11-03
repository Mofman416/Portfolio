# I made this for fun.

import time

def close():
    print("Happy Halloween!")
    print()
    time.sleep(5)
    exit()

print("Happy Halloween!")
print()

while True:
    choice = input("How will you be celebrating? Are you going Trick or Treating, Partying, or Watching Movies? ")
    print()
    if choice.lower().startswith("t"):
        print("So you're going out to get candy? Nice!")
        print()
        while True:
            choice = input("What is your favorite candy? ")
            print()
            if choice.istitle():
                print("That sounds tasty! I'll have to try it sometime.")
                print()
                close()
                break
            else:
                print("What? I couldn't get that. Could you input as a title (i.e. instead of 'snickers' put in 'Snickers').")
                print()
    elif choice.lower().startswith("p"):
        print("That sounds fun!")
        print()
        while True:
            choice = input("Will you be dressing up? Yes or No. ")
            print()
            if choice.lower().startswith("y"):
                print("Cool, I hope you have fun!")
                print()
                close()
                break
            elif choice.lower().startswith("n"):
                print("Ah, that's okay. I don't really have a costume either.")
                print()
                close()
                break
            else:
                print("Sorry, didn't get that, could you try again?")
                print()
    elif choice.lower().startswith("m") or choice.lower().startswith("w"):
        print("Sounds spooky.")
        print()
        while True:
            choice = input("What movie are you watching? ")
            print()
            if choice.istitle():
                print("That sounds interesting!")
                print()
                choice = input("What is it rated? ")
                print()
                if choice.upper() == "G":
                    print("I should show it to my younger siblings.")
                    print()
                    close()
                    break
                elif choice.upper() == "PG":
                    print("Sounds like a pretty cool movie!")
                    print()
                    close()
                    break
                elif choice.upper() == "PG-13":
                    print("I'll have to ask if my family would be interested.")
                    print()
                    close()
                    break
                elif choice.upper() == "R":
                    print("You must be pretty brave! I don't think I could handle that.")
                    print()
                    close()
                    break
                elif choice.upper() == "NC-17":
                    print("DANG!")
                    print()
                    close()
                    break
                else:
                    print("You don't know? Well, that's okay.")
                    print()
                    close()
                    break
    else:
        print("So you're not celebrating? That's okay. Sorry for asking.")
        print()
        close()
        break
        
