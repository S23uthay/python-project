# pong 
# # we need to understand that we have imported turtle, which is a module that provides turtle graphics primitives in both object oriented and procedure oriented ways
# the turtle screen function is used to return the lsit of the turtules on the screen 
import turtle 

wn = turtle.Screen()
wn.title(" pong by @shibi")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)
# Score
score_a = 0
score_b = 0
# paddle A
Pad_A = turtle.Turtle()
Pad_A.speed(0)
Pad_A.shape("square") 
Pad_A.color("white")
Pad_A.shapesize(stretch_wid =5, stretch_len = 1)
Pad_A.penup()
Pad_A.goto(-350,0)
# paddle B
Pad_B = turtle.Turtle()
Pad_B.speed(0)
Pad_B.shape("square") 
Pad_B.color("white")
Pad_B.shapesize(stretch_wid =5, stretch_len = 1)
Pad_B.penup()
Pad_B.goto(350,0)
# Ball 
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square") 
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 2 
Ball.dy = 2
#PENGAME 
PENGAME = turtle.Turtle()
PENGAME.speed(0)
PENGAME.color("white")
PENGAME.penup()
PENGAME.hideturtle()
PENGAME.goto(0,260)
PENGAME.write("Player A: 0  PlayerB: 0", align = "center", font = (" Courier", 24," normal"))

# Function 
def Pad_A_up():
    y = Pad_A.ycor()
    y += 20 
    Pad_A.sety(y)

def Pad_A_down():
    y = Pad_A.ycor()
    y -= 20 
    Pad_A.sety(y)

def Pad_B_up():
    y = Pad_B.ycor()
    y += 20 
    Pad_B.sety(y)

def Pad_B_down():
    y = Pad_B.ycor()
    y -= 20 
    Pad_B.sety(y)

# Keyboard binding 
wn.listen()
wn.onkeypress(Pad_A_up, "w")
wn.onkeypress(Pad_A_down, "s")
wn.onkeypress(Pad_B_up, "Up")
wn.onkeypress(Pad_B_down, "Down")

# Main game loop 
while True: 
    wn.update()

    # Move the Ball 
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor()+ Ball.dy)

    # Border checking 
    if Ball.ycor() > 290: 
        Ball.sety(290)
        Ball.dy *= -1 
        
    if Ball.ycor() < -290: 
        Ball.sety(-290)
        Ball.dy *= -1 
    
    if Ball.xcor() > 390: 
        Ball.goto(0,0)
        Ball.dx *= -1
        score_a += 1
        PENGAME.clear()
        PENGAME.write("Player A: {}  PlayerB: {} ". format(score_a, score_b), align = "center", font = (" Courier", 24," normal"))
    if Ball.xcor() < -390: 
        Ball.goto(0,0)
        Ball.dx *= -1
        score_b += 1
        PENGAME.clear()
        PENGAME.write("Player A: {}  PlayerB: {} ". format(score_a, score_b), align = "center", font = (" Courier", 24," normal"))

    # Paddle and Ball collision 
    if Ball.xcor() < -340 and Ball.ycor() < Pad_A.ycor() + 50 and Ball.ycor() > Pad_A.ycor() - 50:
        Ball.dx *= -1 
    if Ball.xcor() > 340 and Ball.ycor() < Pad_B.ycor() + 50 and Ball.ycor() > Pad_B.ycor() - 50:
        Ball.dx *= -1    
