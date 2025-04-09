import turtle 

t = turtle.Turtle()
t.penup()
t.goto(-100,-100)
t.color("blue")
t.pendown()

for i in range(375):
 t.left(2)
 t.forward(8)
 t.left(3)

for i in range(375):
 t.left(4)
 t.forward(8)
 t.color("red")
 
for i in range(375):
 t.left(6)
 t.forward(10)
 t.color("green")
turtle.exitonclick()