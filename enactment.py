import turtle
import paddle
import ball
import time
import scoreboard
import test
line = turtle.Turtle()
line.color("white")
line.pensize(10)
line.hideturtle()
line.teleport(0, 300)
line.goto(0, -300)
run = test.Test()
r_paddle = paddle.Paddle(350, 0)
l_paddle = paddle.Paddle(-350, 0)
performance = turtle.Screen()
performance.bgcolor("black")
performance.listen()
performance.setup(width = 800, height = 600)
performance.title("Pong Game")
performance.tracer(0)
performance.onkey(key = "Up", fun = r_paddle.go_up)
performance.onkey(key = "Down", fun = r_paddle.go_down)
performance.onkey(key = "w", fun = l_paddle.go_up)
performance.onkey(key = "s", fun = l_paddle.go_down)
object = ball.Ball()
sp = 0.1
game_is_on = True
while game_is_on == True:
    time.sleep(sp)
    performance.update()
    object.go_forward()
    object.collision()
    head = object.heading()
    if object.xcor() >= 330 and object.distance(r_paddle) <= 50:
        sp = sp - sp * 0.1
        if head <= 90:
            object.setheading(head + 2 * (90 - head))
        elif head <= 180:
            object.setheading(head - 2 * (90 - (180 - head)))
        elif head <= 270:
            object.setheading(head + 2 * (270 - head))
        elif head <= 360:
            object.setheading(head - 2 * (90 - (360 - head)))
    if object.xcor() <= -330 and object.distance(l_paddle) <= 50:
        sp = sp - sp * 0.1
        if head <= 90:
            object.setheading(head + 2 * (90 - head))
        elif head <= 180:
            object.setheading(head - 2 * (90 - (180 - head)))
        elif head <= 270:
            object.setheading(head + 2 * (270 - head))
        elif head <= 360:
            object.setheading(head - 2 * (90 - (360 - head)))
    if object.xcor() >= 400:
        sp = 0.1
        object.exaggerate()
        object = ball.Ball()
        run.increaseb()
    if object.xcor() <= -400:
        sp = 0.1
        run.increasea()
        object.exaggerate()
        object = ball.Ball()
performance.exitonclick()