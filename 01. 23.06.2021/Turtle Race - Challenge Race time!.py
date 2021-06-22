#Challenge: Race time!
from turtle import *
from random import randint
speed(10)
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

ron = Turtle()
ron.color('green')
ron.shape('turtle')

ron.penup()
ron.goto(-160, 40)
ron.pendown()

garry = Turtle()
garry.color('yellow')
garry.shape('turtle')

garry.penup()
garry.goto(-160, 10)
garry.pendown()

penup()
goto(-160, 110)
for step in range(15):
  write(step, align = 'center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
for turn in range(100):
  ada.forward(randint(1, 5))
  bob.forward(randint(1, 5))
  ron.forward(randint(1, 5))
  garry.forward(randint(1, 5))
