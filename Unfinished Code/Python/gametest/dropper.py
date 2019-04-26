from superwires import games, color
import random

SCORE = 0

games.init(screen_width=640, screen_height=480, fps=50)

class Fire(games.Sprite):
    image = games.load_image("images/fire.png")



    def __init__(self, x, y=90):
        """Initiate a fire object."""
        super(Fire, self).__init__(Fire.image,
                                   x=x,
                                   y=y,)

        self.speed = random.randint(1, 10)
        self.dy = self.speed

        self.lives = games.Message(value=3, size=25, color=color.black, top=25,
                                   right=games.screen.width - 10)

        self.life_status = games.Message(value="Lives: ", size=25, color=color.black, top=25,
                                         right=games.screen.width - 25)

        games.screen.add(self.lives)
        games.screen.add(self.life_status)

    def update(self):
        """Check if bottom edge has reached screen bottom."""

        if self.bottom > games.screen.height:
            self.lives.value -= 1
            if self.lives.value == 0:
                self.end_game()

            self.destroy()

    def handle_caught(self):
        """Destroys itself once caught."""
        self.destroy()

    def end_game(self):
        """End the game"""

        end_message = games.Message(value="Game Over!", size=90, color=color.blue, x=games.screen.width/2,
                                    y=games.screen.width/2, lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Pyro(games.Sprite):
    """The Pyro who moves left and right, dropping fireballs!"""
    image = games.load_image("images/pyro.png")

    def __init__(self, y=55, speed=2, odds_change=200):
        """Initialize the Chef object"""
        super(Pyro, self).__init__(image=Pyro.image, x=games.screen.width/2, y=y, dx=speed)
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        """Determine if direction needs to be reversed"""

        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()

    def check_drop(self):
        """Decrease countdown or drop pizza and reset countdown"""
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_fire = Fire(x=self.x)
            games.screen.add(new_fire)
        #set buffer to about 30% of pizza height, regardless of pizza speed.
            self.time_til_drop = int(random.randint(1, 10))


class Bucket(games.Sprite):
    """A bucket controlled by the mouse"""
    image = games.load_image("images/bucket.png")

    def __init__(self):
        super(Bucket, self).__init__(image=Bucket.image,
                                     x=games.mouse.x,
                                     bottom=games.screen.height)
        self.score = games.Text(value=0, size=25, color=color.black, top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """Move to mouse coordinates"""
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """Check for collision with fireball"""
        for fire in self.overlapping_sprites:
            self.score.value += 10

            self.score.right = games.screen.width - 10
            fire.handle_caught()

def main():
    # loaded img
    bg_img = games.load_image("images/backgroundedit.PNG", transparent=False)

    # added img to bg
    games.screen.background = bg_img

    # Create Pyro object
    pyro = Pyro()

    bucket = Bucket()

    games.mouse.is_visible = False

    # draws objects to screen
    games.screen.add(pyro)
    games.screen.add(bucket)
    games.screen.event_grab = True

    games.screen.mainloop()


main()
