word = input("Enter a five letter word (i.e. pizza): ")

print(
    """Slicing 'Cheat Sheet'
0 1 2 3 4 5
+---+---+---+---+---+
|"""+word[0]+"""|"""+word[1]+"""|"""+word[2]+"""|"""+word[3]+"""|"""+word[4]+"""|
+---+---+---+---+---+
-5 -4 -3 -2 -1

""")

print(word[0] + word[1] + word[2] + word[3] + word[4])

print("Enter the beginning and ending index for your slice.")
start = None
while start != "":
    start = (input("\nStart: " ))

    if start:
        start = int(start)
        finish = int(input("Finish: "))
        print("word[", start, ":", finish, "] is", end = " ")

        print(word[start:finish])
        time.sleep(2)
        exit()
    break
