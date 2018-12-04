# Michael
#12/04/18
#avg grades

##gradelist = []
##def getGrade(gradelist):
##
##    while True:
##        maxGrade = 100
##        grade = input("Enter a grade. To exit, press the enter key. ")
##        if grade == "":
##            break
##        elif grade.isalnum():
##            grade = float(grade)
##            if grade <= maxGrade:
##                gradelist.append(grade)
##            else:
##                q = input("Are you sure this " + str(grade) + " is a good score? Y/N")
##                if q.lower() == "y":
##                    gradelist.append(grade)
##                else:
##                    print("That is not a good grade.")
##        else:
##            print("Invalid. Please input an integer.")
##
##def avgfunction(gradelist):
##    total = 0
##    for grade in gradelist:
##        total += grade
##    avg = total / len(gradelist)
##    return avg
##
##def main(gradelist):
##
##    getGrade(gradelist)
##    avg = avgfunction(gradelist)
##    xmax = max(gradelist)
##    xmin = min(gradelist)
##    sort(gradelist)
##    print(gradelist)
##    print(xmax)
##    print(xmin)
##    print("Your grade is", avg)
##
##main(gradelist)

start = 5
stop = 1000
stepvalue = 500
for i in range(start,stop,stepvalue):
    print(i)
