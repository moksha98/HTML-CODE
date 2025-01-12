import turtle

turtle.Screen().bgcolor("pink")

a = turtle.Screen()
a.setup(400,300)

turtle.title("Welcomne to turtle")

b = turtle.Turtle()

for i in range(4):
    b.forward(100)
    b.right(90)

turtle.done()