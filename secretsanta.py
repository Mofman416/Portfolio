#Michael Freeman
#12/10/18
#Secret Santa Program

import random
import time

#This list goes down with each new user to signify the turn.
users = ["Dad", "Mom", "Kristopher", "Kourtney", "Brenda", "Michael", "Rebecca", "Allison", "Jonathan", "Cassidy"]

#This is where random names are drawn from. Names will be removed from the list once drawn if they don't match the user name.
names = ["Dad", "Mom", "Kristopher", "Kourtney", "Brenda", "Michael", "Rebecca", "Allison", "Jonathan", "Cassidy"]

#This gets called to get the names of each person.
def get_name():
    while names:
        for i in users:
            print(users[i], "it is your turn to draw.\n")
            input("Make sure nobody is looking and press enter when you are ready.\n")
            
