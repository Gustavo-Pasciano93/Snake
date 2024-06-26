from turtle import Turtle
import random


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()
        
        
    def update_score(self):
        self.clear()
        self.write(f"score = {self.score}  High Score: {self.high_score}", align = "center", font=("Arial", 16, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    
        
    #def game_over(self):
     #   self.goto(0, 0) 
      #  self.write(f"perdeeeeeu", align = "center", font=("Arial", 16, "normal"))
        
        
    def increase_score(self):
        self.score += 1
        
        self.update_score()
        
        
  