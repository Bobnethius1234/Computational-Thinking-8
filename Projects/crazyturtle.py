# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random, sys
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# s1 = create_sprite("dog")
# print(s1.shapesize())


# setup + variables
set_background("park")
s2 = turtle.Turtle()
s1 = turtle.Turtle()
s3 = turtle.Turtle()
s4 = turtle.Turtle()
s5 = create_sprite("appleyay",0,0)
s3.penup()
s4.penup()
s3.goto(-300,200)
s4.goto(-300,150)
s1.penup()
s2.penup()
s1.color("red")
s2.color("blue")
s3.color("red")
s4.color("blue")
# s1 controls
def move_up():
	s1.setheading(90)
	s1.forward(10)
def move_down():
	s1.setheading(270)
	s1.forward(10)
def move_right():
	s1.setheading(0)
	s1.forward(10)
def move_left():
	s1.setheading(180)
	s1.forward(10)
	
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

#controls 
def reset():
	global gameOver
	gameOver += 1
window.onkeypress(reset, "r")

# s2 controls

def move_up():
	s2.setheading(90)
	s2.forward(10)
def move_down():
	s2.setheading(270)
	s2.forward(10)
def move_right():
	s2.setheading(0)
	s2.forward(10)
def move_left():
	s2.setheading(180)
	s2.forward(10)
	
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")




#clear
s3.clear()
s4.clear()
# Section 4: Game Loop
window.listen()
s1.score = -1
s2.score = 0
s1.size = 0
s2.size = 1
gameOver = 0

while True:
	if get_distance(s1,s5) < 30:
		s5.goto(random.randint(-250,250),random.randint(-250,250))
		s1.score += 1
		s3.clear()
		s3.write(s1.score, font = ("Arial", 40, "normal"))
		s1.size += 1
		s1.shapesize(s1.size, s1.size, 1)

	if get_distance(s2,s5) < 30:
		s5.goto(random.randint(-250,250),random.randint(-250,250))
		s2.score += 1
		s4.clear()
		s4.write(s2.score, font = ("Arial", 40, "normal"))
		s2.size += 1
		s2.shapesize(s2.size, s2.size, 1)
	
		
	if s1.score == 10:
		break
	elif s2.score == 10:
		break
	
    
 	# TODO - code for automatic actions






	window.update()

	if gameOver == 1:
		break
	

print("Game Over")
