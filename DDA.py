from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

def dda(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    stepsize = int(max(abs(dx), abs(dy)))

    x_inc = dx / stepsize
    y_inc = dy / stepsize

    x, y = x0, y0
    glBegin(GL_POINTS)
    for _ in range(stepsize + 1):
        glVertex2f(round(x), round(y))
        x += x_inc
        y += y_inc
    glEnd()

pygame.init()
pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)
gluOrtho2D(0, 500, 0, 500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT)
    dda(50, 50, 400, 300)
    pygame.display.flip()
