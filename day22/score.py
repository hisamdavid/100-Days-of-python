from turtle import Turtle

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score=0
    self.r_score=0
    self.updateScore()
  
  def updateScore(self):
    self.clear()
    self.goto(0,200)
    self.write(f"{self.l_score}  {self.r_score}", align="center",font=("Courier", 50, "bold"))