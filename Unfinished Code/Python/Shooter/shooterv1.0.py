# Asteroids 1.0
# Michael Freeman

# imports
from superwires import games
import random

# global info
games.init(screen_width=640, screen_height=480, fps=60)

# classes

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    image = {SMALL : games.load_image("img/meteorsmall.png"),
             MEDIUM : games.load_image("img/meteormedium.png"),
             LARGE : games.load_image("img/meteorlarge.png")}
    SPEED = 2

    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(image=Asteroid.image[size],
                                       x=x,
                                       y=y,
                                       dx=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                       dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        self.size = size

    def update(self):
        if self.right < 0:
            self.left = games.screen.width
        if self.left < 0:
            self.right = games.screen.width
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height

# main
def main():

    #load data
    bg_img = games.load_image("img/space.png")

    #Create objects
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)


    #Draw objects
    games.screen.background = bg_img

    #game setup


    #start main loop
    games.screen.mainloop()

main()
