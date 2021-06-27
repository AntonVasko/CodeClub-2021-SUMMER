#Challenge: More colours!

from turtle import *

screen = Screen()
screen.setup(400, 400)
colours = {'verylime':'#EAEF89', 'rellyrassberry':'#89D6EF', 'awesomeorange':'#F0C33C'}
screen.bgcolor (colours['verylime'])


penup()
goto(0, 100)
color(colours['rellyrassberry'])
style = ('Arial', 40, 'bold')
write('Hello', font=style, align='center')
right(90)
forward(60)
color(colours['awesomeorange'])
write('World', font=style, align='center')
hideturtle()
