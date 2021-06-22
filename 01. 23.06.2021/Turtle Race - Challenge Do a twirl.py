#!/bin/python3
#Challenge: Do a twirl
from turtle import *
from random import randint
speed(10)


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

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
for turn in range(10):
  ada.right(36)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
for turn in range(10):
  bob.right(36)
bob.pendown()

ron = Turtle()
ron.color('green')
ron.shape('turtle')

ron.penup()
ron.goto(-160, 40)
for turn in range(10):
  ron.right(36)
ron.pendown()

garry = Turtle()
garry.color('yellow')
garry.shape('turtle')

garry.penup()
garry.goto(-160, 10)
for turn in range(10):
  garry.right(36)
garry.pendown()

for turn in range(100):
  ada.forward(randint(1, 5))
  bob.forward(randint(1, 5))
  ron.forward(randint(1, 5))
  garry.forward(randint(1, 5))
