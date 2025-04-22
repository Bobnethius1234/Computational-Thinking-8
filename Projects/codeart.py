
import turtle


t = turtle.Turtle()
# background color
turtle.Screen().bgcolor("white")

t.goto(0,0)
t.color ("white")
t.speed(0)

# the colors
colors = ["red","green","blue"]
# drawing
for i in range (5000):
    t.color( colors[ i % 3 ] )
    t.forward(1 + i)
    t.left(429785)

turtle.exitonclick()