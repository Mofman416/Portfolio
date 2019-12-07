#Michael Freeman

import random

names = []

for _ in range(3):
    name = input("\nType in your name. ")
    names.append(name)

while True:
    next = input("\nIs this everyone? Y/N ")
    if next.upper() == 'Y':
        break
    elif next.upper() == 'N':
        name = input("\nType in the next name. ")
        names.insert(0, name)
    else:
        print("\nInvalid response. Please try again.")
print(names)

random.shuffle(names)
pairs = [(first_person, second_person) for first_person, second_person in zip(names, names[1:] + [names[0]])]
print(pairs)
