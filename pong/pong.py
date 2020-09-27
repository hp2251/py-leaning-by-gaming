import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("gray")
window.setup(width=1000, height=800)
window.tracer(0)

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
