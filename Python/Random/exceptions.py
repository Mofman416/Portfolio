##while True:
##    try:
##        num = float(input("Enter a number: "))
##        break
##    except:
##        print("Something went wrong! Enter a number!")
##
##print(num)

##try:
##    num = float(input("\nEnter a number: "))
##except ValueError:
##    print("That is not a number!")
##except NameError:
##    print("Name Error")

##for value in (None, "Hi!"):
##    try:
##        print("Attempting to convert", value, "-->", end = " ")
##        print(float(value))
##    except (TypeError):
##        print("Something went wrong! Type Error")
##    except (ValueError):
##        print("Value Error")

##try:
##    num = float(input("\nEnter a number: "))
##except ValueError as e:
##    print("That's not a number. Or as python would say...")
##    print(e)

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("Not a number!")
else:
    print("You entered the number", num)
