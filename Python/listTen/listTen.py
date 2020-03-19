# Michael Freeman

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

print(a)

print("I want only the numbers that are less than 5 from the list!")

for i in a:
    if i <= 5:
        print(i)

print("How about putting them in a separate list?")

for i in a:
    if i <= 5:
        b.append(i)
print(b)

print("Perfect!")

num = int(input("Now pick a number you'd like to limit the original list to. "))

for i in a:
    if i <= num:
        print(i)
