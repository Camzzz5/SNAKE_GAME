import turtle
POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
MOVE_DISTANCE = 20

class Snake():
    
    def __init__(self,length):
        self.length = length
        self.new_segments = []
        self.create_snake()
        self.head = self.new_segments[0]
        
        
        
    def create_snake(self):       
        for position in POSITIONS:
            self.add_segment(position)
    
    
    def add_segment(self, position):
        segment = turtle.Turtle("square")
        segment.pu()
        segment.color("white")
        segment.goto(position)
        self.new_segments.append(segment)
        
    def extend(self):
        self.add_segment(self.new_segments[-1].position())
        
                 
    def snake_movement(self):
            
        for k in range(len(self.new_segments)-1, 0, -1):
            new_x = self.new_segments[k-1].xcor()
            new_y = self.new_segments[k-1].ycor()
            self.new_segments[k].goto(new_x, new_y)
    
        self.head.fd(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != 270:         
            self.head.setheading(90)
        
    def left(self):
        if self.head.heading() != 0:         
            self.head.setheading(180)
        
    def down(self):
        if self.head.heading() != 90:         
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() != 180:         
            self.head.setheading(0)