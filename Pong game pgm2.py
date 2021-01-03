import turtle
import os
# creating window: 1st  step

wn = turtle.Screen()
wn.title("pong sat")
wn.bgcolor("yellow")
wn.setup(width=800, height=600)
wn.tracer(0)
# (above command - (tracer) its stops that windows from updating so we can manually update and speed up the game
# if we didn't do it its run much much slower)


# score - setting up scores on the points table: 7th step

score_a = 0
score_b = 0

# paddle A:2nd step

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # it avoid to draw a line on window
paddle_a.goto(-340, 0)

# paddle B:2nd step
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # it avoid to draw a line on window
paddle_b.goto(+330, 0)


# ball :2nd step

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()  # it avoid to draw a line on window
ball.goto(0, 0)
ball.dx = 2  # ball moment x to y : 4th step
ball.dy = -2   # ball moment x to y : 4th step

# creating point table pen : 6th step
pen = turtle.Turtle()
pen.speed(0)  # point updating speed
pen.color("green")
pen.penup()
pen.hideturtle()  # hide the turtle on the screen
pen.goto(0, 260)
pen.write("player A: 0  playerB: 0", align="center", font=("Courier", 24, "normal"))

# creating functions for moving paddles: 3rd step

def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
        y =paddle_b.ycor()
        y +=20
        paddle_b.sety(y)

def paddle_b_down():
        y =paddle_b.ycor()
        y -=20
        paddle_b.sety(y)

# keyboard binding: 3rd step

wn.listen()             #(we are informing keyboard to listen us for below procees)
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_down, "Down")


# Mani game  loop: 1st step

while True:
    wn.update()
        # move the ball: 4th step

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # border checking : 4th step

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A: {} player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A: {} player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# paddle and ball collision: 5th step

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() >paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() <-340 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() <paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1







