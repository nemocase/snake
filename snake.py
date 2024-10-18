import turtle
import time
import random 

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("yellowgreen")
window.setup(width=600, height=600)
window.tracer(0)

# Snake head
head = turtle.Turtle() 
head.speed(0) 
head.shape("square")
head.color("black")
head.penup() 
head.goto(0, 0) 
head.direction = "stop" 

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# List
segments = []

# Pen for score tracking
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle() 
pen.goto(0, 260)
pen.write("Score: 0     High Score: 0", align="center", font=("Courier", 24, "bold"))

# Functions
def move():
    if head.direction == "up":
        y = head.ycor() 
        head.sety(y + 20) 
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) 
    if head.direction == "left":
        x = head.xcor() 
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor() 
        head.setx(x + 20) 
    
def go_up():
    if head.direction != "down": 
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

# Key bindings
window.listen() 
window.onkeypress(go_up, "w") 
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# Main game loop
while True:
    window.update() 

    # Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1) 
        head.goto(0,0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000) 
        
        # Clear segments list (otherwise the code below will put them right back in the middle)
        segments.clear()
        
        # Reset time delay
        delay = 0.1

        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))

    # Check for collision with food
    if head.distance(food) < 20: 
        x = random.randint(-290, 290)
        y = random.randint(-290, 290) 
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("sandybrown")
        new_segment.penup()
        segments.append(new_segment)
        
        # Shorten the delay (so it gradually increases in speed as the snake grows)
        delay -= 0.001

        # Increase score
        score += 1
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))

    # Move segments with head
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    # First param (-1) is the start of range; -1 bc list starts at 0, so list of 10 will run 0-9
    # Middle param (0) is end of range; not inclusive so will start at 1
    # Third param (-1) is the increment

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Loop the move function
    move()

    # Check for collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset time delay
            delay = 0.1

            score = 0
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)

# Makes sure the window stays open
window.mainloop()
