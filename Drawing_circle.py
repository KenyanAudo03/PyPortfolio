import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Drawing Circles Practices")


my_turtule = turtle.Turtle()
my_turtule.pensize(5)
my_turtule.color("green")
my_turtule.fillcolor("red")
my_turtule.begin_fill()
my_turtule.circle(100)
my_turtule.end_fill()

turtle.done()