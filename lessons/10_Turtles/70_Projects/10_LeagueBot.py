""" 
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bot.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 
"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')



def set_turtle_image(t, image_name):
   from pathlib import Path
   from PIL import Image
   
   image_dir=Path(__file__).parent.parent / "images"
   image_path = str(image_dir / image_name)
   screen = t.getscreen()
   screen.addshape(image_path)
   t.shape(image_path)


screen=turtle.Screen()
screen.setup(width=600, height=600)
t = turtle.Turtle()
set_turtle_image(t, "leaguebot_bolt.gif")

t.pencolor('blue')
t.forward(100)
t.left(90)
t.forward(100)
t.left(60)
t.forward(100)
















turtle.exitonclick()