#Michael Freeman
#November 30th, 2018

game_list = []
while True:
    option = int(input("""
    1 - Add to List
    2 - Remove from List
    3 - Insert to List
    4 - Exit
    """))
    if option == 1:
        game = input("Please input the title of the game you want to add to your list. ")
        game_list.append(game)
        print(game)
    elif option == 2:
        print(game)
        game = input("Please input the title of the game you want to remove from your list.")
        while True:
            if game in game_list:
                q = input("Are you sure you want", game, "removed from your list?")
                if q == "yes":
                    game_list.remove(game)
                    print(game_list)
                    break
                else:
                    print("Removal canceled.")
            else:
                print(game + " is not on your list.")
    elif option == 3:
        game = input("What game to you want inserted into your list?")
        pos = int(input("Which position should", game, "go?"))
        pos -= 1

        while True:
            if pos <len(game_list):
                game_list.insert(pos,game)
                print(game_list)
                break
            else:
                print("Invalid position")
    elif option == 4:
        print("This is your final game list:\n")
        print(game_list)
        print()
        print("Press enter to exit.")
        break
    else:
        print("Not valid, try again.")
