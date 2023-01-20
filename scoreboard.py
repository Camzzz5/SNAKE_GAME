from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.pu()
        self.color("white")
        self.hideturtle()
        self.goto(0,265)
        self.write(f"scoreboard = {self.score}",move= False, align="center", font =("Arial", 24, "normal"))
        
    def game_over(self):
        self.goto(0,0)  
        self.write(f"Game Over", font =("Arial", 24, "normal"))
                 
    def prompt(self):
        self.clear()
        self.score += 1
        self.write(f"scoreboard = {self.score}",move= False, align="center", font =("Arial", 24, "normal"))
        
        