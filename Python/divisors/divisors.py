# Michael Freeman

newList = []

num = int(input("Pick a number and find it's divisors! "))

divisorList = list(range(2, num+1))

for i in divisorList:
    if num % i == 0:
        newList.append(i)

print(newList)
