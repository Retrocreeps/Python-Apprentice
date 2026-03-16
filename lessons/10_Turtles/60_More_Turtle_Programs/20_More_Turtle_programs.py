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
t1.pendown()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.pendown()
t2.shape("turtle")

#for i in range(-200, 200):
    #t2.goto(i,-i)




def screen_clicked(x, y): 

  print('You pressed: x=' + str(x) + ', y=' + str(y))
  t1.goto(x, y)

screen.onclick(screen_clicked)



def turtle_clicked(t, x, y,):

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
    




t2.onclick(lambda x, y, t=t2: turtle_clicked(t, x, y))
t1.onclick(lambda x, y, t=t1: turtle_clicked(t, x, y))







####t4 = turtle.Turtle()
#t4.penup()
#t4.shape("turtle")

turtle.done()



