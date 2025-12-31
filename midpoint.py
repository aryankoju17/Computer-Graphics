from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

# ---------------- Midpoint Circle Algorithm ----------------
def midpoint_circle(cx, cy, r):
    x = 0
    y = r
    d = 1 - r

    glBegin(GL_POINTS)

    while x <= y:
        # Plot eight symmetric points
        glVertex2i(cx + x, cy + y)
        glVertex2i(cx - x, cy + y)
        glVertex2i(cx + x, cy - y)
        glVertex2i(cx - x, cy - y)

        glVertex2i(cx + y, cy + x)
        glVertex2i(cx - y, cy + x)
        glVertex2i(cx + y, cy - x)
        glVertex2i(cx - y, cy - x)

        # Update decision parameter
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1

        x += 1

    glEnd()

# ---------------- OpenGL Initialization ----------------
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(2.0)
    gluOrtho2D(0, 500, 0, 500)

# ---------------- Main Program ----------------
def main():
    pygame.init()
    pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Midpoint Circle Drawing Algorithm")

    init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        # Draw Circle
        midpoint_circle(250, 250, 150)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
