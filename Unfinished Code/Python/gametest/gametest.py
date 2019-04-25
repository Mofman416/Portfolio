from superwires import games, color
import random

SCORE = 0

games.init(screen_width=640, screen_height=480, fps=50)

class Fire(games.Sprite):

    def update(self):
        """Reverse a velocity component if edge of screen reached"""
        global SCORE
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            SCORE += 1


class Pyro(games.Sprite):

    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx


class ScText(games.Text):
    # Updates the score
    def update(self):
        self.value = SCORE

class Player(games.Sprite):

    def update(self):
        self.dx = 0
        games.keyboard

def main():
    # loaded img
    bg_img = games.load_image("images/backgroundedit.PNG", transparent=False)
    fireball = games.load_image("images/fire.png")
    pyroenemy = games.load_image("images/pyro.png")

    # added img to bg
    games.screen.background = bg_img

    # created fireball object
    fire = Fire(image=fireball,
                        x=games.screen.width/2,
                        y=games.screen.height/2,
                        dx= 5,
                        dy= 0)

    # create text object
    score = ScText(value=SCORE,
                    size=60,
                    color=color.black,
                    x=550,
                    y=30)

    # Create Pyro object
    pyro = Pyro(image=pyroenemy,
                x=games.screen.width/2,
                y=75,
                dx = 5)

    # draws objects to screen
    games.screen.add(fire)
    games.screen.add(score)
    games.screen.add(pyro)

# game_over = games.Message(value="Game Over!",
#                           size=100,
#                           color=color.blue,
#                           x=games.screen.width/2,
#                           y=games.screen.height/2,
#                           lifetime=250,
#                           after_death=games.screen.quit)
# games.screen.add(game_over)



    games.screen.mainloop()

main()