import turtle

def draw_rectangle(start_pos_x, start_pos_y, height, width):
    turtle.penup()
    turtle.setpos(start_pos_x, start_pos_y)
    turtle.pendown()
    turtle.seth(0)
    turtle.begin_fill
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()
    turtle.penup()

def draw_door(start_pos_x, start_pos_y, height, width):
    draw_rectangle(start_pos_x, start_pos_y, height, width)
    turtle.penup()
    turtle.setpos(start_pos_x+3*width/4, start_pos_y+height/2)
    turtle.seth(0)
    turtle.pendown()
    turtle.circle(width/8)
    turtle.penup()

def draw_garage_lines(start_pos_x,start_pos_y, end_pos_x):
    turtle.setpos(start_pos_x, start_pos_y)
    turtle.pendown()
    turtle.setpos(end_pos_x, start_pos_y)
    turtle.penup()

def draw_garage_door(start_pos_x, start_pos_y, height, width, num_lines):
    draw_rectangle(start_pos_x, start_pos_y, height, width)
    for i in range(num_lines-1):
        draw_garage_lines(start_pos_x, start_pos_y + (height*(i+1))/num_lines, start_pos_x + width)


turtle.color('blue', 'yellow')

door_height = 50
door_x = 10
door_y = 0

garage_x = -200
garage_y = 0
garage_height = door_height * 1.3
garage_lines = 4

draw_door(door_x,door_y,door_height, door_height*0.4)
draw_garage_door(garage_x, garage_y, garage_height, garage_height*2.5, garage_lines)

turtle.done()