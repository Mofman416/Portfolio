from superwires import games, color
import random

SCORE = 0

games.init(screen_width=640, screen_height=480, fps=50)

class Fire(games.Sprite):

    def update(self):
        """Reverse a velocity component if edge of screen reached"""
        global SCORE
        # if self.right > games.screen.width or self.left < 0:
        #     self.dx = -self.dx
        #     SCORE += 1

        ##FIGURE THIS OUT!!
        if self.left > games.screen.height:
            self.x = games.screen.width/2
            self.dx = 0
            self.dy = 5
            SCORE += 1
        if self.top < 0:
            self.right = 0
            self.dy = self.dx
            SCORE += 1
        if self.left > games.screen.width:
            self.top = 0
            self.dx = -self.dy
            SCORE += 1
        if self.right < 0:
            self.bottom = games.screen.height
            self.dx = self.dy
            SCORE += 1


class ScText(games.Text):
    #updates the score
    def update(self):
        self.value = SCORE

def main():
    #loaded img
    bg_img = games.load_image("images/backgroundedit.PNG", transparent=False)
    fireball = games.load_image("images/fire.png")

    #added img to bg
    games.screen.background = bg_img

    #created firball object
    fire = Fire(image=fireball,
                        x=games.screen.width/2,
                        y=games.screen.height/2,
                        dx= 5,
                        dy= 0)


    #create text object
    score = ScText(value=SCORE,
                    size=60,
                    color=color.black,
                    x=550,
                    y=30)

    #draws objects to screen
    games.screen.add(fire)
    games.screen.add(score)

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