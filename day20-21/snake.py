from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  
  def __init__(self) :
    self.segments=[]
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for segment in range(3):
      x_position=segment*-20
      self.add_segment((x_position,0))

  def move(self):
    for seg_num in range(len(self.segments)-1,0,-1):
      next_segment_pos=self.segments[seg_num-1].pos()
      self.segments[seg_num].goto(next_segment_pos)
    self.head.forward(10)

  def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

  def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

  def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

  def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

  def add_segment(self,position):
      new_segment=Turtle("square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(x=position[0],y=position[1])
      self.segments.append(new_segment)

  def extend(self):
      self.add_segment(self.segments[-1].position())
      