# Asteroids 1.0
# Michael Freeman
# Work on the lives system.

# imports
from superwires import games, color
import random
import math

# global info
games.init(screen_width=640, screen_height=480, fps=60)


# classes

class Game(object):
    def __init__(self):
        # set level
        self.level = 0
        # load sound for level advance
        self.sound = games.load_sound("sounds/mvm_used_powerup.ogg")
        # create score
        self.score = games.Text(value=0,
                                size=30,
                                color=color.white,
                                top=5,
                                right=games.screen.width - 10,
                                is_collideable=False)
        games.screen.add(self.score)
        self.create_ship()

    def create_ship(self):
        self.ship = Ship(game=self,
                          x=games.screen.width / 2,
                          y=games.screen.height / 2)
        games.screen.add(self.ship)

    def play(self):
        games.music.load("sounds/Erebus.ogg")
        games.music.play(-1)

        bg_img = games.load_image("img/space.png")
        games.screen.background = bg_img

        self.advance()

        games.screen.mainloop()

    def advance(self):
        self.level += 1
        # amount of space around ship to preserve when creating asteroids.
        BUFFER = 150

        # Create objects
        for i in range(self.level):
            # calculate an x and y at least BUFFER distance from the ship
            # choose minimum distance along x-axis and y-axis
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            # choose distance along x-axis and y-axis based on minimum distance
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)
            #calculate location based on distance
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance
            # wrap around screen, if necessary
            x %= games.screen.width
            y %= games.screen.height

            size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])

            new_asteroid = Asteroid(game=self, x=x, y=y, size=Asteroid.LARGE)
            games.screen.add(new_asteroid)

        # display level number
        level_message = games.Message(value="Level " + str(self.level),
                                      size=40,
                                      color=color.yellow,
                                      x=games.screen.width/2,
                                      y=games.screen.height/10,
                                      lifetime=3 * games.screen.fps,
                                      is_collideable=False)
        games.screen.add(level_message)

        # play new level sound (except at first level)
        if self.level > 1:
            self.sound.play()

    def end(self):
        """End the game."""
        # show 'Game Over' for 5 seconds
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)



class Wrapper(games.Sprite):
    def update(self):
        if self.right < 0:
            self.left = games.screen.width

        if self.left > games.screen.width:
            self.right = 0

        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

    def die(self):
        self.destroy()


class Collider(Wrapper):
    def update(self):
        """Check for overlapping sprites."""
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        # create explosion
        new_explosion = Explosion(obj_x=self.x, obj_y=self.y)
        # add screen
        games.screen.add(new_explosion)
        self.destroy()


class Ship(Collider):
    image = games.load_image("img/ship.png")
    sound = games.load_sound("sounds/thrusters.ogg")

    ROTATION_STEP = 7
    VELOCITY_STEP = .03
    MISSILE_DELAY = 25
    VELOCITY_MAX = 3
    LIVES = 3

    def __init__(self, game, x, y):
        super(Ship, self).__init__(image=Ship.image, x=x, y=y)
        self.game = game
        self.missile_wait = 0
        self.lives = games.Text(value=Ship.LIVES, size=25, color=color.white, top=25,
                                right=games.screen.width - 10, is_collideable=False)
        self.life_status = games.Message(value="Lives: ", size=25, color=color.white, top=25,
                                         right=games.screen.width - 25, is_collideable=False)

        games.screen.add(self.lives)
        games.screen.add(self.life_status)

    def update(self):
        super(Ship, self).update()
        self.lives.destroy()
        self.lives = games.Text(value=Ship.LIVES, size=25, color=color.white, top=25,
                                right=games.screen.width - 10, is_collideable=False)
        games.screen.add(self.lives)
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_UP) or games.keyboard.is_pressed(games.K_w):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
        if self.missile_wait > 0:
            self.missile_wait -= 1

        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

    def loselife(self):
        self.lives.value -= 1
        Ship.LIVES -= 1
        self.game.create_ship()
        if self.lives.value == 0:
            self.die()
            self.game.end()

    def die(self):
        super(Ship, self).die()
        self.loselife()




class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    image = {SMALL: games.load_image("img/meteorsmall.png"),
             MEDIUM: games.load_image("img/meteormedium.png"),
             LARGE: games.load_image("img/meteorlarge.png")}
    SPEED = 2

    SPAWN = 2

    POINTS = 30

    total = 0

    def __init__(self, game, x, y, size):
        Asteroid.total += 1

        super(Asteroid, self).__init__(image=Asteroid.image[size],
                                       x=x,
                                       y=y,
                                       dx=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                       dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        self.size = size
        self.game = game

    def die(self):
        # if asteroid isn't small, replace with two smaller asteroids
        Asteroid.total -= 1
        # add to score
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10

        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game=self.game, x=self.x,
                                        y=self.y,
                                        size=self.size - 1)
                games.screen.add(new_asteroid)
        self.destroy()

        if Asteroid.total == 0:
            self.game.advance()
        super(Asteroid, self).die()


class Missile(Collider):
    image = games.load_image("img/lasere.png")
    sound = games.load_sound("sounds/laser.ogg")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        Missile.sound.play()
        angle = ship_angle * math.pi / 180

        # calculate missile's starting position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)

        x = ship_x + buffer_x
        y = ship_y + buffer_y

        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        super(Missile, self).__init__(image=Missile.image,
                                      x=x,
                                      y=y,
                                      dx=dx,
                                      dy=dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        super(Missile, self).update()
        # if lifetime is up, destroy the missile
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Explosion(games.Animation):
    sound = games.load_sound("sounds/mvm_tank_explode.ogg")
    expimages = ["img/explosion1.bmp",
                 "img/explosion2.bmp",
                 "img/explosion3.bmp",
                 "img/explosion4.bmp",
                 "img/explosion5.bmp",
                 "img/explosion6.bmp",
                 "img/explosion7.bmp",
                 "img/explosion8.bmp",
                 "img/explosion9.bmp"]

    def __init__(self, obj_x, obj_y):
        super(Explosion, self).__init__(images=Explosion.expimages,
                                        x=obj_x,
                                        y=obj_y,
                                        repeat_interval=4,
                                        n_repeats=1,
                                        is_collideable=False)
        Explosion.sound.play()


# main
def main():
    asteroids = Game()
    asteroids.play()


main()
