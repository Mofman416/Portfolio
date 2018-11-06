##Pseudocode:
##num1: input from the user;
##num2: input from the user;
##
##check numbers if num1 and num2 are all digits
##If both are digits tell user
##If one or the other is a digit tell user
##If neither are digits tell user.


num1 =input("Enter a number ")
num2 =input("Enter a number ")
if num1.isdigit() and num2.isdigit():
    print("Both numbers are digits")
elif num1.isdigit() or num2.isdigit():
    print("One of the numbers are digits")
else:
    print("Neither are numbers.")
