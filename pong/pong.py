import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("gray")
window.setup(width=1000, height=800)
window.tracer(0)

# Main game loop
while True:
    window.update()
