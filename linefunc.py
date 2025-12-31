from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import random

# ---------------- DDA Line Function ----------------
def dda_line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x0, y0

    glBegin(GL_POINTS)
    for _ in range(steps + 1):
        glVertex2i(round(x), round(y))
        x += x_inc
        y += y_inc
    glEnd()

# ---------------- Generate Line Graph ----------------
def generate_line_graph(n, x_margin, y_min, y_max, width):
    points = []
    gap = (width - 2 * x_margin) / (n - 1)
    for i in range(n):
        x = x_margin + i * gap
        y = random.randint(y_min, y_max)
        points.append((x, y))
    return points

# ---------------- OpenGL Initialization ----------------
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(0.0, 1.0, 1.0)
    glPointSize(2.0)
    gluOrtho2D(0, 500, 0, 500)

# ---------------- Main Program ----------------
def main():
    pygame.init()
    pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Line Graph using DDA Algorithm")
    init()

    n_points = 10
    x_margin = 50
    y_min, y_max = 50, 450
    width = 500

    points = generate_line_graph(n_points, x_margin, y_min, y_max, width)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        # Draw line graph using DDA between consecutive points
        for i in range(len(points) - 1):
            x0, y0 = points[i]
            x1, y1 = points[i + 1]
            dda_line(x0, y0, x1, y1)

        pygame.display.flip()
        pygame.time.wait(50)

    pygame.quit()

if __name__ == "__main__":
    main()
