name = input("What's your name? ")
age = input("How old are you? ")
##if name.isalpha() and age.isdigit() and name.istitle() and age<"20" and age >"15" or name =="Michael":
##    print("You're in.")
##else:
##    print("Kick rocks, punk!")
##    

if age>"70" or age<"15":
    print("Yeah you're old enough to drive.")
elif age>"70":
    print("You be too old to drive")
elif age<"15":
    print("You be too young to drive.")
else:
    print("Don't drive. Please.")
