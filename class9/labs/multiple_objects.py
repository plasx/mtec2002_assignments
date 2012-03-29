"""
multiple_objects.py
===
Try animating multiple objects.  Rather than storing x and y directly in variables, we can store them in a 2 element list as coordinates.  To easily iterate through all of these coordinates, we can put all of them into another list.  Generally, the strategy will be:

1. Create 2-element lists to represent coordinates:
	a. for example... [5, 29]
	b. the x coordinate is 5
	c. the y coordinate is 29
2. Initialize the list of coordinates during the setup part of the program.
3. In the main loop, iterate through all of the coordinates and adjust the x and y values (the 2 element list and index 0 and 1) appropriately.

To code this:
1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Create the following variables above the main loop:
	a. a constant (all caps) called NUM_CIRCLES ...set it equal to the number of objects you'd like to animate
	b. an empty list called circles
	c. a variable called r that holds the radius of your circles - set it equal to a value below 10 
	d. a variable called velocity_y; set it equal to how fast you want your circles to move (below 5 is good)
3. Create a for loop that loops for as many times as the value you have in NUM_CIRCLES.
4. In each iteration, append a 2 element list to your circles list:
	a. the first value, which represents x, should be a random value between 0 and the width of your screen
	b. the second value, which represents y, should be 0
5. In the main loop, iterate through every element in the circles list
6. Draw a circle for each iteration using the 2-element list at index 0 for the x value and index 1 for the y value
7. Add velocity_y to the 2-element list at index 1 (the y coordinate)
"""
import pygame
import random

FRAME_RATE = 60
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "MONEY MAKING Game"
NUM_CIRCLES = 105
circles =[]
velocity_y = 10
r = 5
for c in range(NUM_CIRCLES):
		circles.append([random.randint(0, WINDOW_WIDTH), 0])

background_color = (255, 255, 0)
running = True
pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

while running == True:

	# stop the main loop when window is closed 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	screen.fill(background_color)
	for c in circles:
			pygame.draw.circle(screen, (0,0,200),(c[0],c[1]), 10)
			c[1] += velocity_y
			if c[1] >= WINDOW_HEIGHT:
					c[1] = 1
	# draw everything here!  this line draws a circle in the middle of the screen
	pygame.draw.circle(screen, (0, 0, 200), (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), 10)

	clock.tick(FRAME_RATE)
	pygame.display.flip()
