# Import a library of functions called 'pygame'
import pygame
from math import pi

# CORES
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
GREY = (128,128,128)
GREY31 = (79,79,79)
GAINSBORO = (220,220,220)

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = [800, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Arvore AVL")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(WHITE)

    # Draw lines
    pygame.draw.aaline(screen, GAINSBORO, [400, 100],[350, 175], True)
    pygame.draw.aaline(screen, GAINSBORO, [400, 100],[450, 175], True)
    pygame.draw.aaline(screen, GAINSBORO, [350, 175],[250, 250], True)
    pygame.draw.aaline(screen, GAINSBORO, [350, 175],[350, 250], True)
    pygame.draw.aaline(screen, GAINSBORO, [450, 175],[450, 250], True)
    pygame.draw.aaline(screen, GAINSBORO, [450, 175],[550, 250], True)
    pygame.draw.aaline(screen, GAINSBORO, [250, 250],[135, 325], True)
    pygame.draw.aaline(screen, GAINSBORO, [250, 250],[210, 325], True)
    pygame.draw.aaline(screen, GAINSBORO, [350, 250],[285, 325], True)
    pygame.draw.aaline(screen, GAINSBORO, [350, 250],[360, 325], True)
    pygame.draw.aaline(screen, GAINSBORO, [450, 250],[435, 325], True)
    pygame.draw.aaline(screen, GAINSBORO, [450, 250],[510, 325], True)
    pygame.draw.aaline(screen, GAINSBORO, [550, 250],[585, 325], True)
    pygame.draw.aaline(screen, GAINSBORO, [550, 250],[660, 325], True)

    # Draw a circle
    pygame.draw.circle(screen, GAINSBORO, [400, 100], 25)#1
    pygame.draw.circle(screen, GAINSBORO, [350, 175], 25)#2
    pygame.draw.circle(screen, GAINSBORO, [450, 175], 25)#3
    pygame.draw.circle(screen, GAINSBORO, [250, 250], 25)#4
    pygame.draw.circle(screen, GAINSBORO, [350, 250], 25)#5
    pygame.draw.circle(screen, GAINSBORO, [450, 250], 25)#6
    pygame.draw.circle(screen, GAINSBORO, [550, 250], 25)#7
    pygame.draw.circle(screen, GAINSBORO, [135, 325], 25)#8
    pygame.draw.circle(screen, GAINSBORO, [210, 325], 25)#9
    pygame.draw.circle(screen, GAINSBORO, [285, 325], 25)#10
    pygame.draw.circle(screen, GAINSBORO, [360, 325], 25)#11
    pygame.draw.circle(screen, GAINSBORO, [435, 325], 25)#12
    pygame.draw.circle(screen, GAINSBORO, [510, 325], 25)#13
    pygame.draw.circle(screen, GAINSBORO, [585, 325], 25)#14
    pygame.draw.circle(screen, GAINSBORO, [660, 325], 25)#15


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
