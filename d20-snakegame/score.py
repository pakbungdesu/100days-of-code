

from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 13, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.score = 0
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGN, font=FONT)
        self.goto(0, -20)
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

