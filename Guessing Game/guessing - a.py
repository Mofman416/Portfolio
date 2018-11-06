def advanced():
    while True:
        choice = input("Would you like to change the number range (N) or the amount of guesses (G)? ")
        print()
        if choice.lower().startswith("n"):
            low = input("Please set the lowest number: ")
            print()
            if low.isdigit():
                high = print("Please set the highest number: ")
                print()
                if high.isdigit() and high > low:
                    game()
                    break
                else:
                    print("Please input a valid number or choose a number higher than the lower number.")
                    print()
            else:
                print("Please input a valid number.")
                print()
        elif choice.lower().startswith("g"):
            guess = input("Please set the number of guesses. ")
            print()
            if guess.isdigit():
                game()
                break
            else:
                print("Please input a valid integer.")
                print()
    return

advanced()
            
