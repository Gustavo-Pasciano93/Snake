from turtle import Turtle, Screen

START_POSITIONS = [(0,0), (-10,0), (-20,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head =self.segments[0]
        
    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
            
            
    def add_segment(self, position):
        cobra = Turtle()
        cobra.shape("square")
        cobra.shapesize(0.5, 0.5)
        cobra.color("white")
        cobra.penup()
        cobra.goto(position)
        self.segments.append(cobra)
        
    
    
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
            
            
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
        
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
        
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
        
    