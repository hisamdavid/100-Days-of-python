from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score=-1
    self.color("white")
    self.penup()
    self.hideturtle()
    self.refresh_score()

  def refresh_score(self):
    self.clear()
    self.goto(x=0,y=260)
    self.score+=1
    self.write(f"Score: {self.score}",True,"center",font=('Arial', 15, 'normal'))

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER.",True,"center",font=('Arial', 15, 'normal'))