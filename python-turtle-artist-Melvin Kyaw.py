import turtle
import random


screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)


def draw_grass():
    """Draws a patch of green grass at the bottom."""
    t.penup()
    t.goto(-400, -200)
    t.pendown()
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()


draw_grass()


flower_colors = ["red", "orange", "yellow", "magenta", "purple", "pink"]
center_colors = ["gold", "white", "brown"]
flower_count = 10

for i in range(flower_count):
    x = random.randint(-350, 350)
    y = random.randint(-150, 100)
    petal_color = random.choice(flower_colors)
    center_color = random.choice(center_colors)
    petal_size = random.randint(10, 30)


def draw_sun():
    """Draws a bright yellow sun in the sky."""
    t.penup()
    t.goto(250, 180)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()


draw_sun()


t.hideturtle()
turtle.done()
