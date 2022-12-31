# Imports all the available pygame modules into the pygame package.
import pygame
# Optional, puts a limited set of 280 constants and functions into the global namespace of your script e.g. key modifiers.
from pygame.locals import *
import math

# Initialize all the pygame modules
pygame.init()

width, height = 800, 800
size = width, height

# Set display mode
# pygame.display.set_mode((width, height), flags, depth)
screen = pygame.display.set_mode(size)

# Set the current window caption
window_caption = 'Planets'
pygame.display.set_caption(window_caption)

# create an object to help track time
clock = pygame.time.Clock()

# SETTING CONSTANTS

# Colors defined as tuples of the base colors red, green and blue (the RGB model), then assigned to variables.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

fps = 50                    # frames per second (max 60), time between frames = 1/fps

sf = 1 / 13926800     # scaling factor: scale from meters to pixels

# BALL
v = 40                      # speed: pixels per second
x = 100                     # x position, center of circle
y = 100                     # y position, center of circle
radius = 20
width = 0                   # zero radius = fill circle

#Avo = 6.02e23
Avo = 100000000000000
softening = 0.1

# The Sun
sun_radius = 50
sun_x, sun_y = 400, 400
#sun_x, sun_y = width // 2, height // 2  # center sun on screen, uses floor division to round down
sun_mass = 1.989e30

# Venus
venus_radius = 20
venus_mass = 4.87e24
venus_x, venus_y = sun_x, sun_y - 100   # x, y coordinates
venus_vx, venus_vy = 400, 0           # velocities
venus_ax, venus_ay = 0, 0               # accelerations

# Earth
earth_radius = 25
earth_mass = 5.97e24
earth_x, earth_y = sun_x, sun_y - 200
earth_vx, earth_vy = 1, 0
earth_ax, earth_ay = 0, 0

# Mars
mars_radius = 15
mars_mass = 6.39e23
mars_x, mars_y = sun_x, sun_y - 300
mars_vx, mars_vy = 1, 0
mars_ax, mars_ay = 0, 0

# Time variables
time_elapsed = 0
time_step = 0.000000000000000000000008




# INITIAL CONDITIONS

#background = RED
#screen.fill(background)
#pygame.display.update()

running = True
# The event loop
while running:
    # quit out if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Increase/decrease ball velocity with arrow keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            v += 5    
        elif event.key == pygame.K_LEFT:
            v -= 5

    screen.fill(BLACK)  # blank screen prior to redraw

    # Draw ball
    x += v / fps    # New x-position iterated (pixels)  
    pygame.draw.circle(screen, RED, (x, y), radius, width)  # Draw object in memory


    # Draw sun
    pygame.draw.circle(screen, WHITE, (sun_x, sun_y), sun_radius)

    # Draw Venus
    pygame.draw.circle(screen, WHITE, (venus_x, venus_y), venus_radius)
    #pygame.draw.ellipse(screen, WHITE, (sun_x - 100, sun_y - 150, 200, 300), 1)

    # Draw Earth
    pygame.draw.circle(screen, WHITE, (earth_x, earth_y), earth_radius)
    #pygame.draw.ellipse(screen, WHITE, (sun_x - 200, sun_y - 250, 400, 500), 1)

    # Draw Mars
    pygame.draw.circle(screen, WHITE, (mars_x, mars_y), mars_radius)
    #pygame.draw.ellipse(screen, WHITE, (sun_x - 300, sun_y - 350, 600, 700), 1)

    pygame.display.flip()   # Redraw i.e. Update the full display Surface to the screen

    # Update planet positions using Kepler's laws of planetary motion


    # F = m1a = Gm1m2/r^2
    # a = Gm2/r^2
    # Planet acceleration = G * sun_mass / distancebetween squared
    # Velocity update = acceleration * dt

    venus_ax += -Avo * sun_mass / (((venus_x - sun_x) + softening)**2)
    venus_ay += -Avo * sun_mass / (((venus_y - sun_y) + softening)**2)
    venus_vx += venus_ax * time_step
    venus_vy += venus_ay * time_step
    venus_x += venus_vx * time_step     # position = velocity * time step
    venus_y += venus_vy * time_step

    earth_ax += Avo * sun_mass / (((earth_x - sun_x) + softening)**2)
    earth_ay += Avo * sun_mass / (((earth_y - sun_y) + softening)**2)
    earth_vx += earth_ax * time_step
    earth_vy += earth_ay * time_step
    earth_x += earth_vx * time_step
    earth_y += earth_vy * time_step
    
    mars_ax += Avo * sun_mass / (((mars_x - sun_x) + softening)**2)
    mars_ay += Avo * sun_mass / (((mars_y - sun_y) + softening)**2)
    mars_vx += mars_ax * time_step
    mars_vy += mars_ay * time_step
    mars_x += mars_vx * time_step
    mars_y += mars_vy * time_step

    # Update time elapsed
    time_elapsed += time_step













    clock.tick(fps) # delay by 1/fps seconds
     

pygame.quit()

