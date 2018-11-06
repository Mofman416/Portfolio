#Michael Freeman

#November 6th 2018

import random

name = "Michael Freeman"

print(name[-4])
length =len(name)
print(length)
index_pos = random.randrange(0, length)
if index_pos<=length:
    char = name[index_pos]
else:
    print("That's out of the range.")
