from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

# ---------------- Bresenham Algorithm ----------------
def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Direction of movement
    sx = 1 if x1 >= x0 else -1
    sy = 1 if y1 >= y0 else -1

    x, y = x0, y0

    glBegin(GL_POINTS)

    # -------- Case 1: |m| < 1 (dx > dy) --------
    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            glVertex2i(x, y)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * (dy - dx)
            else:
                p += 2 * dy

    # -------- Case 2: |m| >= 1 (dy >= dx) --------
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            glVertex2i(x, y)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * (dx - dy)
            else:
                p += 2 * dx

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
    pygame.display.set_caption("Bresenham Line Drawing Algorithm")

    init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        # Case 1: |m| < 1
        bresenham_line(50, 100, 450, 250)

        # Case 2: |m| >= 1
        bresenham_line(200, 50, 300, 450)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
