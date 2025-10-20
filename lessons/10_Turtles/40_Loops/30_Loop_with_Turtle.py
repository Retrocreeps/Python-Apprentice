"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )
"""

... # Your code here
import turtle
turtle.setup(600,600,0,0)
tina = turtle.Turtle()
tina.shape(turtle)
tina.speed(2)
tina.forward(150)
tina.left(45)
tina.forward(150)
tina.left(45)
tina.forward(150)
tina.left(45)
tina.forward(150)
tina.left(45)
tina.forward(150)
tina.left(45)

for i in range(4):
    print ('Loop Iteration', i)

turtle.exitonclick