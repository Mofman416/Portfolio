##word = input("Enter a word. ")
##print()
##print("\nHere's each letter in your word:")
##print()
##for letter in word:
##    print(letter)
##    print()
##print(len(word))

##message = input ("Input a message: ")
##new_message = ""
##VOWELS = "aeiouy"
##for letter in message:
##    if letter.lower() not in VOWELS:
##        new_message += letter
##        print("A new string has been created:", new_message)
##print("\nYour message without vowels is:", new_message)

print("Counting:")
for i in range(10):
    print(i, end=" ")

print("\n\nCounting by Fives:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nCounting Backwards:")
for i in range(10, 0, -1):
    print(i, end="")
