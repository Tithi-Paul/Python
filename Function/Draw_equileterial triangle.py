import turtle

#turtle.shape("turtle")
turtle.speed(2) #0 means highest speed. 1 means lowest speed. Gradually increase till 10.

def equilateral_triangle(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

counter = 0
while counter < 120 :
    equilateral_triangle(100)
    turtle.right(3)
    counter += 1

turtle.exitonclick()