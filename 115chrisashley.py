#   a115_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

lines = 6
length = 50
spacing = 90 / lines
ladybug.pensize(5)
count = 0
while (count < lines):
  ladybug.goto(0,-40)
  ladybug.setheading(spacing*count)
  if(count==0):
    ladybug.setheading(-30)
  if(count==1):
    ladybug.setheading(0)
  if(count==2):
    ladybug.setheading(30)
  if(count==3):
    ladybug.setheading(150)
  if(count==4):
    ladybug.setheading(180)
  if(count==5):
    ladybug.setheading(-150)
  ladybug.forward(length)
  count = count + 1
ladybug.penup()
ladybug.goto(0,0)
ladybug.pendown()

ladybug.color("red")
# and body
ladybug.penup()
ladybug.setheading(0)
ladybug.goto(0, -55) 
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
dots = 1
xpos = -25
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 32, ypos + 15)
  ladybug.pendown()
  ladybug.circle(2)
  xpos=xpos+10
  ypos=ypos+18
  dots=dots+1


ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()