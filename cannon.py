"""David Antonio Zarate Villaseñor A01665896
Christopher Gordillo Dominguez A01666339"""

"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def reposition_target(target):
    """Reposition the target when it leaves the screen."""
    target.x = 200
    target.y = randrange(-150, 150)


def reposition_ball():
    """Reposition the ball when it leaves the screen."""
    ball.x = -199
    ball.y = -199


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
      
        if not inside(target):
		reposition_target(target)	
	else:
		target.x -= 2.0
    if inside(ball):
        speed.y -= 0.2
        ball.move(speed)
	# Reposition the ball if it leaves the screen
        if not inside(ball):
            reposition_ball()

    for target in targets:
        if abs(target - ball) < 13:
            reposition_target(target)
            
            
    draw()

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
