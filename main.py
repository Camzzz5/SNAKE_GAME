import turtle
import time
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


new_segments = []
for i in range(3):
    segment = turtle.Turtle("square")
    segment.pu()
    segment.color("white")
    segment.goto(-20*i, 0)
    new_segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for k in range(len(new_segments)-1, 0, -1):
        new_x = new_segments[k-1].xcor()
        new_y = new_segments[k-1].ycor()
        new_segments[k].goto(new_x, new_y)
    
    new_segments[0].fd(20)
    
        
screen.exitonclick()


