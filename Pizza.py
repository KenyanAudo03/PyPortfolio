#Using turtle
import turtle
BACKGROUND_COLOR = "#9EC388"
CRUST_COLOR = "#ECA84F"
SAUCE_COLOR = "#AD0509"
CHEESE_COLOR = "#FBC70F"
PEPERONI_LOCATIONS = [
    [-70, 105],
    [-85, 175],
    [-25, 50],
    [-15, 100],
    [-25, 150],
    [-30, 205],
    [15, 50],
    [20, 120],
    [20, 200],
    [60, 156],
    [71, 215],
    [80, 90],
    [95, 150]
]

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("My Pizza")

my_turtule = turtle.Turtle()
my_turtule.pensize(5)
my_turtule.shape("circle")

def draw_circle(radius, line_color, fill_color):
    my_turtule.color(line_color)
    my_turtule.fillcolor(fill_color)
    my_turtule.begin_fill()
    my_turtule.circle(radius)
    my_turtule.end_fill()

def move_turtle(x, y):
    my_turtule.up()
    my_turtule.goto(x, y)
    my_turtule.down()

draw_circle(150, CRUST_COLOR, CRUST_COLOR)
move_turtle(0, 25)
draw_circle(125, SAUCE_COLOR, CHEESE_COLOR)

for location in PEPERONI_LOCATIONS:
    move_turtle(location[0], location[1])
    draw_circle(10,SAUCE_COLOR,SAUCE_COLOR)

move_turtle(0, 150)
my_turtule.color(BACKGROUND_COLOR)

for x in range(0, 8):
    my_turtule.pendown()
    my_turtule.left(45)
    my_turtule.forward(150)
    my_turtule.penup()
    my_turtule.backward(150)


turtle.done()


# #Using pygame
# import pygame
# import sys
# import math

# # Define colors
# BACKGROUND_COLOR = (158, 195, 136)
# CRUST_COLOR = (236, 168, 79)
# SAUCE_COLOR = (173, 5, 9)
# CHEESE_COLOR = (251, 199, 15)
# PEPPERONI_COLOR = SAUCE_COLOR

# # Pepperoni locations
# PEPPERONI_LOCATIONS = [
#     [-70, -105],
#     [-85, -175],
#     [-25, -50],
#     [-15, -100],
#     [-25, -150],
#     [-30, -205],
#     [15, -50],
#     [20, -120],
#     [20, -200],
#     [60, -156],
#     [71, -215],
#     [80, -90],
#     [95, -150]
# ]

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# screen_size = (400, 400)
# screen = pygame.display.set_mode(screen_size)
# pygame.display.set_caption("My Pizza")

# # Create clock object to control frame rate
# clock = pygame.time.Clock()

# # Main drawing function
# def draw_pizza():
#     # Draw crust
#     pygame.draw.circle(screen, CRUST_COLOR, (200, 200), 150)

#     # Draw sauce and cheese
#     pygame.draw.circle(screen, SAUCE_COLOR, (200, 200), 125)
#     pygame.draw.circle(screen, CHEESE_COLOR, (200, 200), 120)

#     # Draw pizza slices
#     for angle in range(0, 360, 45):
#         x1 = 200 + int(150 * math.cos(math.radians(angle)))
#         y1 = 200 + int(150 * math.sin(math.radians(angle)))
#         x2 = 200 + int(120 * math.cos(math.radians(angle)))
#         y2 = 200 + int(120 * math.sin(math.radians(angle)))
#         pygame.draw.line(screen, BACKGROUND_COLOR, (200, 200), (x1, y1), 5)

#     # Draw pepperoni
#     for location in PEPPERONI_LOCATIONS:
#         pygame.draw.circle(screen, PEPPERONI_COLOR, (int(location[0] + 190), int(location[1] + 330)), 8)

# # Main loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Clear the screen
#     screen.fill(BACKGROUND_COLOR)

#     # Draw the pizza
#     draw_pizza()

#     # Update the display
#     pygame.display.flip()

#     # Set the frame rate
#     clock.tick(30)
