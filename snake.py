import turtle as t
import random as rand
import time as ti

t.bgcolor('yellow')

snake = t.Turtle()
snake.shape('square')
snake.speed(0)
snake.penup()
snake.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf' , leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed()
leaf.hideturtle()

text = False
text = t.Turtle()
text.write('press space to start', align = 'center', font= ('Arial' , 18,'bold') )
text.hideturtle()

score = t.Turtle()
score.hideturtle()
score.speed(0)

def outsideWindw():
    leftwall = -t.window_width()/2
    rightwall = t.window_width()/2
    topwall = t.window_height()/2
    bottomwall = -t.window_height()/2
    (x,y) = snake.pos()
    outside = x < leftwall or x > rightwall or y > topwall or y < bottomwall
    return outside

def leafPlace():
    leaf.hideturtle()
    leaf.setx(rand.randint(-200,200))
    leaf.sety(rand.randint(-200,200))
    leaf.showturtle()

def gameOver():
    snake.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER', align = 'center', font= ('Arial' , 40 ,'bold'))

def dispalyScore(current_score):
    score.clear()
    score.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 50
    score.setpos(x,y)
    score.write(str(current_score) , align = 'right', font= ('Arial' , 15 ,'normal'))

def startgame():
    global game_started
    #if game_started:

    #    return
    game_started = True
    s = 0
    text.clear()
    snake_speed = 3
    snake_length = 2
    snake.shapesize(1, snake_length , 1)
    snake.showturtle()
    dispalyScore(s)
    leafPlace()

    while True:
        snake.forward(snake_speed)
        if snake.distance(leaf) < 20:
            leafPlace()
            snake_length = snake_length + 1
            snake_speed = snake_speed +1
            snake.shapesize (1, snake_length , 1)
            s = s +10
            dispalyScore(s)
        if outsideWindw():
            gameOver()
            break
def move_up():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)
def move_down():
    if snake.heading() == 0 or snake.heading()== 180:
        snake.setheading(270)
def move_right():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)
def move_left():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)


t.onkey(startgame,'space')
t.onkey(move_up , 'Up')
t.onkey(move_down , 'Down')
t.onkey(move_left , 'Left')
t.onkey(move_right , 'Right')
t.listen()
t.mainloop()


ti.sleep(3)
