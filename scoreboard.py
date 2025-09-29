from turtle import Turtle
ALIGNMENT = 'left'
FONT =  ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        with open("high_scores.txt") as previous_high_score:
            self.highscore = int(previous_high_score.read())
        self.hideturtle()
        self.color("white")
        self.goto(-150,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}  High Score = {self.highscore}"  , align=ALIGNMENT, font=FONT )


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        self.score = 0
        self.update_scoreboard()

