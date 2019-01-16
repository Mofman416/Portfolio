#This is an example of classes
class Human(object):

    def __init__(self,name,hair_color,eye_color,height,weight,iq,gender,race):
        self.name=name
        self.hair_color=hair_color
        self.eye_color=eye_color
        self.height=height
        self.weight=weight
        self.iq=iq
        self.gender=gender
        self.race=race
    def intro_self(self):
        print("Hello. The name's "+self.name)
    def describe_self(self):
        print("I have "+self.hair_color+ " hair")
        print("I have "+self.eye_color+" eyes")
        print("I am",self.height,"inches tall")
        print("I weigh",self.weight,"lbs")
        print("I am a "+self.race+" "+self.gender+" with an iq of ",self.iq)
    def learn(self):
        print("Alright "+self.name+" how about you take a quiz to bump up that IQ of ", self.iq)
        answer = input("What is 2+2? ")
        if answer.isdigit():
            if int(answer)==4:
                print("You go it!")
                self.iq += 1
                print("Your IQ is now", self.iq)
            else:
                print("Wrong!")
        else:
            print("Invalid input!")
    def bmi(self):
        print("Let's find out what your BMI is given you weight of", self.weight, "and your height of", self.height, "\n")
        num1 = self.weight*0.45
        num2 = self.height*0.025
        num3 = num2*num2
        bmi = num1//num3
        print("With you weight and height put through functions and math, you BMI is", bmi, "\n")
        if bmi >= 12 and bmi <=18:
            print("You are underweight!")
        elif bmi >=18 and bmi <=24:
            print("You are at a healthy weight for your height!")
        elif bmi >= 25 and bmi <= 29:
            print("You are overweight!")
        elif bmi >= 30 and bmi <= 39:
            print("You are obese!")
        elif bmi >= 40 and bmi <= 42:
            print("You are extremely obese!")
        else:
            print("Sorry, I can't seem to calculate your BMI. This could be due to either too low or too high BMI.")


            
            
mike = Human("Mike", "Brown", "Hazel", 72, 151, 90, "Male", "White")
mike.intro_self()
mike.describe_self()
mike.learn()
mike.bmi()

#Make a function to calculare the BMI of an individual. Compare it to a BMI chart
