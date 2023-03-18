from turtle import Turtle, Screen


class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.level = 1
        self.update_levelboard()


    def raise_level(self):
        self.level += 1

    def update_levelboard(self):
        self.clear()
        self.goto(-260, 170)
        self.write(f"Level: {self.level}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 15, "normal"))