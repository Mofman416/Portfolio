###Michael Freeman
###9/18
import math
##
###get a users name
##def get_name():
### step one ask user for name
## name=input("What's you name? ")
### step two display the name
##print("the name you entered was", name)
### step three verify the name
##print("Is this correct? Yes or No: ")
##get_name()


###calculate the area of a circle
###radius*radius*pi
##def areaOfCircle ():
###1 Get a Radius
##    radius = input("What is the Radius")
###2 Calculate the Area
##    radius = int(radius)
##    area=radius*radius*3.14159
###3 Display Area
##    print("The area of a Circle is: ", area)
##areaOfCircle()

def pythagoras_theorem(ap=1,bp=1):
    a=float(a)
    b=float(b)
    c=a*a+b*b
    c=math.sqrt(c)

    print("the third side is",c)

##pythagoras_theorem(3,4)

def add_numbers(x,y):
    num1=x
    print("num1 = x", num1)
    num2=y
    print("num2 = y", num2)
    num3= int(num1)+int(num2)
    return num3

x=1
y=-9
num4 = add_numbers(x,y)
print(num4)

