"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""



import turtle as turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)

t1 = turtle.Turtle()
t1.penup()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.penup
t2.shape("arrow")

for i in range(-200, 200):
    t1.goto(i,i)
    t2.goto(i,-i)


import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

t = turtle.Turtle()
t.penup()
t.shape("turtle")

def screen_clicked(x, y): 

print('You pressed: x=' + str(x) + ', y=' + str(y)) 
t.goto(x, y)

import turtle as turtle 
turtle.setup(width=600, height=600)
t = turtle.Turtle()
t.shape("turtle")
t.turtlesize(stretch_wid=10, stetch_len=10, outline=4)

def turtle_clicked(t, x, y):

print('turtle clicked!')

for i in range(0,360, 20):
    t.tilt(20)

t.onlick(lambda x, y, t=t: turtle_clicked(t, x, y))





