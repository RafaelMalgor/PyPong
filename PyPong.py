import turtle


def setup_bar(x, y):
    bar = turtle.Turtle()
    bar.speed(0)
    bar.shape("square")
    bar.color("yellow")
    bar.shapesize(stretch_wid=5, stretch_len=1)
    bar.penup()
    bar.goto(x, y)
    return bar


def update_score(writer):
    writer.clear()
    writer.write(f"Left: {left_score}     Right: {right_score}",
                 align="center", font=("Courier", 24, "bold"))


def bar_up(bar):
    def up():
        y = bar.ycor()
        y += 20
        bar.sety(y)
    return up


def bar_down(bar):
    def down():
        y = bar.ycor()
        y -= 20
        bar.sety(y)
    return down


window = turtle.Screen()
window.title("Simple Pong with Turtle")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)


# Left Player
left_bar = setup_bar(-350, 0)

# Right Player
right_bar = setup_bar(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

# Score
left_score = 0
right_score = 0

score_w = turtle.Turtle()
score_w.speed(0)
score_w.color("red")
score_w.penup()
score_w.hideturtle()
score_w.goto(0, 260)


window.listen()
window.onkeypress(bar_up(left_bar), "w")
window.onkeypress(bar_down(left_bar), "s")
window.onkeypress(bar_up(right_bar), "Up")
window.onkeypress(bar_down(right_bar), "Down")

update_score(score_w)
# Game loop
while True:
    window.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        left_score += 1
        update_score(score_w)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        right_score += 1
        update_score(score_w)

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_bar.ycor() + 40 and ball.ycor() > right_bar.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_bar.ycor() + 40 and ball.ycor() > left_bar.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
