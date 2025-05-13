# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
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
s3.penup()
s4.penup()
s3.goto(-300,200)
s4.goto(-300,150)
s1.penup()
s2.penup()
s1_score = 0
s2_score = 0
s3.write(s1_score, font = ("Arial", 40, "normal"))
s4.write(s2_score, font = ("Arial", 40, "normal"))

# s1 controls
def move_up():
	s1.setheading(90)
	s1.forward(5)
def move_down():
	s1.setheading(270)
	s1.forward(5)
def move_right():
	s1.setheading(0)
	s1.forward(5)
def move_left():
	s1.setheading(180)
	s1.forward(5)
	
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")



# s2 controls

def move_up():
	s2.setheading(90)
	s2.forward(5)
def move_down():
	s2.setheading(270)
	s2.forward(5)
def move_right():
	s2.setheading(0)
	s2.forward(5)
def move_left():
	s2.setheading(180)
	s2.forward(5)
	
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")


# # create_sprite("dog")

# s2.resizemode("user")
# s2.shapesize(5,5, 1)
# print(s2.shapesize())
# Section 3: Controls
# TODO - define your controls
# TODO - pick keys for each control


# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 	# TODO - code for automatic actions






	window.update()

	# if :
	# 	break
	

print("Game Over")
