"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

... # Copy code to make a turtle and set up the window

t = ... # Create a turtle named t

# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.


    


# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.





import turtle
turtle.setup(600,600,0,0)

tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(3)

for i in range(40): 
    tina.pencolor("red")
    tina.forward(30)
    tina.pencolor ("orange")
    tina.forward(30)
    tina.pencolor("yellow")
    tina.forward(30)
    tina.pencolor("green")
    tina.forward(30)
    tina.pencolor("lime")
    tina.forward(30)
    tina.pencolor("teal")
    tina.forward(30)
    tina.left(115)
    tina.pencolor("cyan")
    tina.forward(30)
    tina.pencolor("blue")
    tina.forward(30)
    tina.pencolor("aqua")
    tina.forward(30)
    tina.pencolor("purple")
    tina.forward(30)
    tina.pencolor("magenta")
    tina.forward(30)
    tina.pencolor("pink")
    tina.forward(30)
    tina.left(115)














turtle.exitonclick()