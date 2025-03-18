###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("park")

q1 = codesters.Square(100, 100, 200, 'black')
q2 = codesters.Square(-100, 100, 200, 'red')
q3 = codesters.Square(-100, -100, 200, 'blue')
q4 = codesters.Square(100, -100, 200, 'white')

s1 = codesters.Sprite("desktop", 100, -100)
s1.set_size(.75)
s2 = codesters.Sprite("cardinal", -100, 100)
s3 = codesters.Sprite("sanfran", -100, -100)
s3.set_size(.6)
s4 = codesters.Sprite("basketball2", 100, 100)
s4.set_size(1)

message1 = codesters.Text("Arin Mookherjee-Smith",0,220,"blue")
message2 = codesters.Text("this is my coat of arms -->",0,-220,"black")