from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)
missile_sound = games.load_sound("sounds/laser.mp4")
games.music.load("sounds/Erebus.mp4")

choice = None
while choice != 0:
    choice = input("Choice: ")
    print()

    if choice == "0":
        print("Good-Bye.")

    elif choice == "1":
        missile_sound.play()
        print("Playing missile sound.")

    elif choice == "2":
        loop = int(input("Loop how many extra times? (-1 = forever)"))
        missile_sound.play(loop)
        print("Looping missile sound.")
    elif choice == "3":
        missile_sound.stop()
        print("Stopping missile sound.")

    elif choice == "4":
        games.music.play()
        print("Playing theme song.")

    elif choice == "5":
        loop = int(input("Loop how many extra times? (-1 = forever)"))
        games.music.play(loop)
        print("Looping missile sound.")
    elif choice == "6":
        games.music.stop()
        print("Stopping missile sound.")

    else:
        print("\nSorry, but", choice, "isn't a valid choice.")