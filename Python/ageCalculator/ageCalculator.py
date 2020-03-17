# Michael Freeman

name = input("What is your name? ")
age = int(input("How old are you now? "))

final = ((2020 - age) +100)

i = int(input("How many times would you like to see the resulting message? "))
runs = 0

while runs <= i:
    print(name, "will be 100 years old in", final, "\n")
    runs = runs + 1
