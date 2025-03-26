# Beginning: create variables
MichaelScott_points = 0
JimHalpert_points = 0
KevinMalone_points = 0

print("take this quiz to figure out what character from The Office you are")

# Middle: Ask questions
answer = input("You are on your lunch break, you have 1hr, what do you do? A) hang out with your friends B) pull a prank C) eat lunch")
if answer == "B":
    JimHalpert_points += 1
elif answer == "A":
    MichaelScott_points += 1
elif answer == "C":
    KevinMalone_points += 1

answer = input("you are invited to a dinner party at a co-workers house, what do you do? A) eat dinner as fast as possible"
"   B) try to get out of going C) enjoy the dinner party and socialize   ")
if answer == "A":
    KevinMalone_points += 1
elif answer == "B":
    JimHalpert_points += 1
elif answer == "C":
    MichaelScott_points += 1

answer = input("your boss doesn't show up to work! what do you do?  A) have fun by yourself in the office  B) do work by yourself in the office  C) go home and enjoy the rest of your day")
if answer == "A":
    MichaelScott_points += 1
elif answer == "B" :
    KevinMalone_points += 1
elif answer == "C":
    JimHalpert_points += 1

answer = input("you spent all night making chili, but when you bring it to work, you spill it! what do you do? A) sit and cry  B) clean it up C) go crazy and punch the wall ")
if answer == "A":
    KevinMalone_points += 1
elif answer == "B":
    JimHalpert_points += 1
elif answer == "C":
    MichaelScott_points += 1

answer = input("toby (annoying co-worker) walks into the office, what do you do?  A) attack him  B) say hi to him  C) mock him")
if answer == "A":
    MichaelScott_points += 1
elif answer == "B":
    JimHalpert_points += 1
elif answer == "C":
    KevinMalone_points += 1

#End calculate results
if MichaelScott_points > JimHalpert_points and MichaelScott_points > KevinMalone_points:
    print("You are Michael Scott!")
elif JimHalpert_points > KevinMalone_points and JimHalpert_points > MichaelScott_points: 
    print("you are Jim Halpert!")
elif KevinMalone_points > MichaelScott_points and KevinMalone_points > JimHalpert_points:
    print("you are Kevin Malone!")