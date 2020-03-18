# Michael Freeman

num = int(input("Please input a number. "))

if num % 2 == 0:
    if num % 4 == 0:
        print("This is an even number that is a divisible by 4!")
    else:
        print("This is an even number!")
else:
    print("This is an odd number!")

print("For my next trick, I need two numbers.")

num2 = int(input("Please enter a number. "))
check = int(input("Input a number to check divisibility with. "))

if num2 % check == 0:
    print(num2, "divides evenly with", check)
else:
    print(num2, "does not divide evenly with", check)
