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
t2.shape("turtle")

for i in range(-200, 200):
    t1.goto(i,i)
    t2.goto(i,-i)


import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

t3 = turtle.Turtle()
t3.penup()
t3.shape("turtle")

def screen_clicked(x, y): 

  print('You pressed: x=' + str(x) + ', y=' + str(y))
  t.goto(x, y)

import turtle as turtle 
turtle.setup(width=600, height=600)
t4 = turtle.Turtle()
t4.shape("turtle")
#t.turtlesize(stretch_wid=10, stetch_len=10, outline=4)

def turtle_clicked(t, x, y):

  print('turtle clicked!')


  for i in range(0,360, 20):
    t.pencolor("red")
    t.left(20)
    t.forward(20)
    t.pencolor("orange")
    t.left(20)
    t.forward(20)
    t.pencolor("yellow")
    t.left(20)
    t.forward(20)
    t.pencolor("green")
    t.left(20)
    t.forward(20)
    t.pencolor("lime")
    t.left(20)
    t.forward(20)
    t.pencolor("cyan")
    t.left(20)
    t.forward(20)
    t.pencolor("blue")
    t.left(20)
    t.forward(20)
    t.pencolor("purple")
    t.left(20)
    t.forward(20)
    t.pencolor("magenta")
    t.left(20)
    t.forward(20)
    t.pencolor("pink")
    t.left(20)
    t.forward(20)
    


t4.onclick(lambda x, y, t=t4: turtle_clicked(t, x, y))
t3.onclick(lambda x, y, t=t3: turtle_clicked(t, x, y))
t2.onclick(lambda x, y, t=t2: turtle_clicked(t, x, y))
t1.onclick(lambda x, y, t=t1: turtle_clicked(t, x, y))





turtle.done()
t3.goto(200, 200)


