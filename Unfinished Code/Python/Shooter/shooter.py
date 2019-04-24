# Read Key
#Demonstrates reading the keyboard

from superwires import games

games.init(screen_width = 640, screen_height=480, fps=50)

class Ship(games.Sprite):
    ship_image = games.load_image("img/ship.png")

    def __init__(self):
        super(Ship, self).__init__(image = Ship.ship_image,
                                  x = games.screen.width/2,
                                  y = games.screen.height/2)

def main():

    #load Data
    nebula_image = games.load_image("img/space.png", transparent=False)

    #create objects
    the_ship = Ship()

    #draw
    games.screen.background = nebula_image
    games.screen.add(the_ship)


    #game setup

    #start loop
    games.screen.mainloop()

main()