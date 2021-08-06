import turtle
import random

screen = turtle.Screen()
screen.setup(1920, 1080)
screen.bgcolor("#6eb6fa")
screen.tracer(0)
screen.addshape("Spacebattle - Assets/X-Ela.gif")
screen.addshape("Spacebattle - Assets/Virus.gif")
screen.addshape("Spacebattle - Assets/Antidote.gif")

class Enemy:
    def __init__(self):
        self.enemy_turtle = turtle.Turtle()
        self.enemy_turtle.shape("Spacebattle - Assets/Virus.gif")
        self.enemy_turtle.penup()
        self.enemy_turtle.hideturtle()
        self.enemy_turtle.goto(random.randint(0, 300), random.randint(-450, 500))
        self.enemy_turtle.showturtle()

    def move_up(self):
        y = self.enemy_turtle.ycor()
        y += random.randint(1, 2)
        self.enemy_turtle.sety(y)

    def move_down(self):
        y = self.enemy_turtle.ycor()
        y -= random.randint(1, 2)
        self.enemy_turtle.sety(y)

class Ship:
    def __init__(self, name, pilot):
        self.name = name
        self.pilot = pilot
        self.ship_turtle = turtle.Turtle()
        self.ship_turtle.shape("Spacebattle - Assets/X-Ela.gif")
        self.ship_turtle.penup()
        self.ship_turtle.speed(0)
        self.ship_turtle.hideturtle()
        self.ship_turtle.goto(-500, 0)
        self.ship_turtle.showturtle()
        self.ship_orientation = "None"

        self.lazer_turtle = turtle.Turtle()
        self.lazer_turtle.shape("Spacebattle - Assets/Antidote.gif")
        self.lazer_turtle.penup()
        self.lazer_turtle.speed(0)
        self.lazer_turtle.hideturtle()
        self.lazer_turtle.goto(-500, 0)
        self.lazer_state = "Ready"

    def move_up(self):
        self.ship_orientation = "Up"

    def move_down(self):
        self.ship_orientation = "Down"

    def fire(self):
        print(self.lazer_state)
        if(self.lazer_state == "Ready"):
            self.lazer_state = "Fire"
            x = self.ship_turtle.xcor()
            y = self.ship_turtle.ycor()
            self.lazer_turtle.goto(x, y)
            self.lazer_turtle.showturtle()

alex_ship = Ship("X_Ela", "Alex")
screen.onkey(alex_ship.move_up, "w")
screen.onkey(alex_ship.move_down, "s")
screen.onkey(alex_ship.fire, "space")
screen.listen()

score = 0
enemies = []
enemy_count = 10



for i in range(10):
    enemy_ship = Enemy()
    enemies.append(enemy_ship)

while True:
    screen.update()

    #Ship Movement
    if(alex_ship.ship_orientation == "Up"):
        y = alex_ship.ship_turtle.ycor()
        y += 1
        alex_ship.ship_turtle.sety(y)
    if (alex_ship.ship_orientation == "Down"):
        y = alex_ship.ship_turtle.ycor()
        y -= 1
        alex_ship.ship_turtle.sety(y)

    #Ship Borders
    if(alex_ship.ship_turtle.ycor() >= 500):
        alex_ship.ship_turtle.sety(500)
    if (alex_ship.ship_turtle.ycor() <= -450):
        alex_ship.ship_turtle.sety(-450)

    #Fire
    if(alex_ship.lazer_state == "Fire"):
        x = alex_ship.lazer_turtle.xcor()
        y = alex_ship.lazer_turtle.ycor()
        x += 4
        alex_ship.lazer_turtle.setx(x)

    #Fire Border
    if(alex_ship.lazer_turtle.xcor() >= 900):
        alex_ship.lazer_state = "Ready"
        alex_ship.lazer_turtle.hideturtle()

    #Enemy Events
    for enemy_ship in enemies:
        #Enemy Movements
        move = random.randint(1, 2)
        if(move == 1):
            enemy_ship.move_up()
        else:
            enemy_ship.move_down()

        #Fire Collision
        if(enemy_ship.enemy_turtle.distance(alex_ship.lazer_turtle) <= 20):
            enemy_ship.enemy_turtle.hideturtle()
            enemy_ship.enemy_turtle.goto(2000, 2000)
            enemy_count -= 1

    #Exit Game
    if(enemy_count <= 0):
        break
