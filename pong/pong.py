import turtle
import winsound

window = turtle.Screen()
window.title("Pong")
window.bgcolor("gray")
window.setup(width=1000, height=800)
window.tracer(0)

# Score
leftPlayerScore = 0
rightPlayerScore = 0

# Left Paddle
leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("black")
leftPaddle.shapesize(stretch_wid=6, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-450, 0)

# Right Paddle
rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("black")
rightPaddle.shapesize(stretch_wid=6, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Left Player: 0, Right Player: 0", align="center",
          font=("Courier", 24, "normal"))

# Functions


def leftPaddleUp():
    currentYCor = leftPaddle.ycor()
    currentYCor += 20
    leftPaddle.sety(currentYCor)


def leftPaddleDown():
    currentYCor = leftPaddle.ycor()
    currentYCor -= 20
    leftPaddle.sety(currentYCor)


def rightPaddleUp():
    currentYCor = rightPaddle.ycor()
    currentYCor += 20
    rightPaddle.sety(currentYCor)


def rightPaddleDown():
    currentYCor = rightPaddle.ycor()
    currentYCor -= 20
    rightPaddle.sety(currentYCor)


# Keyboard binding
window.listen()
window.onkeypress(leftPaddleUp, "w")
window.onkeypress(leftPaddleDown, "s")
window.onkeypress(rightPaddleUp, "Up")
window.onkeypress(rightPaddleDown, "Down")


# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)

    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 520:
        ball.goto(0, 0)
        ball.dx *= -1
        leftPlayerScore += 1
        pen.clear()
        pen.write("Left Player: {}, Right Player: {}".format(leftPlayerScore, rightPlayerScore), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -520:
        ball.goto(0, 0)
        ball.dx *= -1
        rightPlayerScore += 1
        pen.clear()
        pen.write("Left Player: {}, Right Player: {}".format(leftPlayerScore, rightPlayerScore), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < rightPaddle.ycor() + 50 and ball.ycor() > rightPaddle.ycor() - 50):
        ball.setx(440)
        ball.dx *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)

    if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < leftPaddle.ycor() + 50 and ball.ycor() > leftPaddle.ycor() - 50):
        ball.setx(-440)
        ball.dx *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
