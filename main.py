import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

serpiente = Snake(3)
food = Food()
scoreboard = Scoreboard()
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
        scoreboard.prompt()
        serpiente.extend()
        
    if serpiente.head.xcor() < -280 or serpiente.head.xcor() > 280 or serpiente.head.ycor() < -280 or serpiente.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over() 
    
    for segmento in serpiente.new_segments[1:]:
        if serpiente.head.distance(segmento) < 10:
            game_is_on = False
            scoreboard.game_over() 
            
        
screen.exitonclick()


