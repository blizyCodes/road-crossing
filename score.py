FONT = ("Courier", 24, "normal")


from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(-240, 270)
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.update_score()

    def increment(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(
            f"Level:  {self.score}",
            align="center",
            font=("Arial", 18, "normal"),
        )

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(
            f"GAME OVER",
            align="center",
            font=("Arial", 35, "normal"),
        )
