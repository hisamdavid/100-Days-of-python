from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    self.xmov=10
    self.ymov=10
    self.movspeed=0.1

  def move(self):
    new_x=self.xcor() + self.xmov
    new_y=self.ycor() + self.ymov
    self.goto(new_x,new_y)

  def bounceOnWall(self):
    self.ymov *= -1

  def bounceOnPaddle(self):
    self.xmov *= -1
    self.movspeed *= 0.9

  def resetPos(self):
    self.goto(0,0)
    self.movspeed=0.1
    self.bounceOnPaddle()
