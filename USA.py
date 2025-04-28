import turtle
t = turtle.Turtle()

# setup
t.speed(0)
turtle.Screen().bgcolor("light blue")


# stripes

# move to stripe 1
t.goto(-250, -100)
h = 50

# stripe 1
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, -50)

# stripe 2
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 3
t.goto(-250, 0)

# stripe 3
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 4
t.goto(-250, 50)

# stripe 4
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 5
t.goto(-250, 100)

# stripe 5
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()


# blue square
t.goto(-50, 0)
t.color("gold")
t.begin_fill()
for i in range(5):
 t.forward(150)
 t.left(144)
t.end_fill()
turtle.exitonclick()

# w vietnam flag