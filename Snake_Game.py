
import turtle,random,time

screen = turtle.Screen()
turtle.bgcolor('yellow')

screen.setup(height = 700, width = 600)
screen.tracer(0)
screen.title('Snake Game')


# max = turtle.Turtle()
# max.color('red')
# max.circle(200)   


turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-290,250)
turtle.pendown()
turtle.forward(575)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(575)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
# turtle.forward(600)
turtle.penup ()
turtle.hideturtle()



# making Snake 

snake = turtle.Turtle()
snake.speed(0)
snake.color('black')
snake.shape('square')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'



#  food
food = turtle.Turtle()
food.color('red')
food.shape('circle')
food.penup()
food.goto(100,20)

score = 0
delay = 0.3

# scoring    Main     Heading

scoring = turtle.Turtle()
scoring.color('blue')
scoring.speed(0)
scoring.penup()
scoring.goto(0,300)
scoring.hideturtle()
scoring.write('Score Bord : ',align="center",font=("poppins",24,'bold'))


def snake_go_up():
    if snake.direction != "down":
        snake.direction  = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction  = "down"
def snake_go_left():
    if snake.direction != "right":
        snake.direction  = "left"
def snake_go_right():
    if snake.direction != "left":
        snake.direction  = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y -20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_left,"Left")
screen.onkeypress(snake_go_right,"Right")

old_food = []

while True:
    screen.update()
    if snake.distance(food) < 20:
        x = random.randint(-270,250)
        y = random.randint(-240,240)
        food.goto(x,y)

        scoring.clear()
        score +=1
        scoring.write(f"Score{score}",align='center',font=("poppins",24,'bold'))
        delay  -=0.001

        # creating new food
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape('square')
        new_food.color('red')
        new_food.penup()
        old_food.append(new_food)

    # addig onside tail part 

    for index in range (len(old_food) -1,0,-1):
        a = old_food[index-1].xcor()
        b = old_food[index-1].ycor()

        old_food[index].goto(a,b)

    if len(old_food) >0:

        a = snake.xcor()
        b = snake.ycor()
        old_food[0].goto(a,b)

    snake_move()
    time.sleep(delay)

    if snake.xcor() > 270 or snake.xcor() < -240 or snake.ycor() > 270 or snake.ycor()<-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("black")
        scoring.goto(0,0)
        scoring.write(f"Game Over \n your score is {score}" ,align = "center", font=("poppins",24,'bold'))
    for fruit in old_food:

        if fruit.distance(snake) < 20 :
            time.sleep(1)
            screen.clear()
            screen.bgcolor("black")
            scoring.goto(0,0)
            scoring.write(f"Game Over \n your score is {score}" ,align = "center", font=("poppins",24,'bold'))

    time.sleep(delay)