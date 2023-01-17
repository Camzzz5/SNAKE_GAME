import turtle
import time
from snake import Snake
from food import Food

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

serpiente = Snake(3)
food = Food()
screen.listen()
screen.onkey(serpiente.up,"Up")
screen.onkey(serpiente.left,"Left")
screen.onkey(serpiente.right,"Right")
screen.onkey(serpiente.down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    serpiente.snake_movement()

    if serpiente.head.distance(food) <= 15:
        food.refresh()
        

    
        
screen.exitonclick()

