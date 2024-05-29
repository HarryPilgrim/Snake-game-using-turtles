from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(0,260)
        self.color("white")

        self.write(f"score: {self.score}, high score: {self.high_score}", align = "center",  font=("ariel", 15, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

            self.write_score()
        self.score = 0


    # def game_over(self):
    #     self.home()
    #
    #     self.write("GAME OVER",  align = "center",  font=("ariel", 40, "normal"))
    def write_score(self):
        self.clear()
        self.write(f"score: {self.score}, high score: {self.high_score}", align="center",
                   font=("ariel", 15, "normal"))

    def get_score(self):

        self.score += 1
        self.write_score()


