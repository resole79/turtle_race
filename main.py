from turtle import Turtle, Screen
import random

# Declare Variable
x = 500
y = 400
list_of_turtle = []
image = "./image/background_turtle_race.png"
color = ["red", "orange", "yellow", "green", "blue", "purple"]
race = False

# screen
screen = Screen()
screen.title("Welcome to the turtle race!")
screen.bgpic(image)
screen.setup(x, y)
bet = screen.textinput("Make your bet", "Which turtle will win the race?")

# Message turtle
message = Turtle()
message.penup()
message.hideturtle()
message.goto(5, -160)

if bet:
    race = True

# Initialize position turtle
y_position = ((-y/2)+5)
x_position = ((x/2)-20)

# Cycle for to read all Color in list
for turtles_color in color:
    # Create turtle for race
    y_position += 30
    turtle_name = Turtle()
    turtle_name.shape("turtle")
    turtle_name.penup()
    turtle_name.color(turtles_color)
    turtle_name.goto(-x_position, y_position)
    turtle_name.speed("fastest")
    list_of_turtle.append(turtle_name)

# Cycle "While" condition to exit race equal False
while race:
    # Cycle for to read all turtle in list
    for turtle in list_of_turtle:
        # if condition to check position turtle
        if turtle.xcor() < x_position:
            random_step = random.randint(1, 10)
            turtle.forward(random_step)
        else:
            # race finish
            turtle_win = turtle.pencolor().capitalize()
            race = False

            print("Your bet: ", bet.capitalize())
            print("The winner: ",turtle_win)

            if bet == turtle_win[0]:
                message.write(f"You've win!\nThe {turtle_win} turtle is the winner", align="center", font=("Cooper Black", 15, "italic"))
            else:
                message.write(f"You've lost!\nThe {turtle_win} turtle is the winner", align="center", font=("Cooper Black", 15, "italic"))

screen.exitonclick()
