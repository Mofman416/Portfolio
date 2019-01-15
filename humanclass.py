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
        print("I am",self.height,"tall")
        print("I weigh",self.weight,"lbs")
        print("I am a "+self.race+" "+self.gender+" with an iq of ",self.iq)
    def learn(self):
        print("Alright "+self.name+" how about you take a quiz to bump up that IQ of ", self.iq)
        answer = input("What is 2+2? ")
        if answer.isdigit():
            if int(answer)==4:
                print("You go it!")
                self.iq += 1
                print(self.)
            else:
                print("Wrong!")
        else:
            print("Invalid input!")
            
            
mike = Human("Mike", "Brown", "Hazel", 6, 151, 90, "Male", "White")
mike.intro_self()
mike.describe_self()
mike.learn()

#Make a function to calculare the BMI of an individual. Compare it to a BMI chart
