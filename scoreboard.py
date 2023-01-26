from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.pu()
        self.color("white")
        self.hideturtle()
        self.goto(0,265)
        self.write(f"scoreboard = {self.score}",move= False, align="center", font =("Arial", 24, "normal"))
        
    def game_over(self):
        self.goto(0,0)  
        self.write(f"Game Over",  align="center", font =("Arial", 24, "normal"))
                 
    def prompt(self):
        self.clear()
        self.write(f"scoreboard = {self.score} High score = {self.high_score} ",move= False, align="center", font =("Arial", 24, "normal"))
        
    def reset(self):
        if self.score > self.high_score: 
            self.high_score = self.score
        self.score = 0
        self.prompt()
        
    def increase_score(self):
        self.score += 1
        self.prompt()
           