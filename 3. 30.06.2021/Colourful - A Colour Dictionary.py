#A Colour Dictionary

from turtle import *

screen = Screen()
screen.setup(400, 400)
colours = {'verylime':'#EAEF89', 'rellyrassberry':'#89D6EF'}
screen.bgcolor (colours['verylime'])

color(colours['rellyrassberry'])
style = ('Arial', 40, 'bold')
write('Hello', font=style, align='center')
hideturtle()
