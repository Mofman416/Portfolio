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

    def update(self):
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            self.y -= 10
        if games.keyboard.is_pressed(games.K_s) or games.keyboard.is_pressed(games.K_DOWN):
            self.y += 10
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 10
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 10

        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270


def main():

    #load Data
    nebula_image = games.load_image("img/space.png", transparent=False)
    explosion_files = ["img/explosion1.bmp", "img/explosion2.bmp", "img/explosion3.bmp",
                       "img/explosion4.bmp", "img/explosion5.bmp", "img/explosion6.bmp",
                       "img/explosion7.bmp", "img/explosion8.bmp", "img/explosion9.bmp"]

    missile_sound = games.load_sound("sounds/laser.mp4")
    games.music.load("sounds/Erebus.mp4")

    #create objects
    the_ship = Ship()
    explosion = games.Animation(images=explosion_files,
                                x=games.screen.width/2,
                                y=games.screen.height/2,
                                n_repeats=5,
                                repeat_interval=5)

    #draw
    games.screen.background = nebula_image
    games.screen.add(the_ship)
    games.screen.add(explosion)


    #game setup

    #start loop
    games.screen.mainloop()

main()