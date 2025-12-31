import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ---------------- Plot Symmetric Points ----------------
def plot_ellipse_points(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)

# ---------------- Midpoint Ellipse Algorithm ----------------
def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    # Region 1 decision parameter
    p1 = ry2 - rx2 * ry + 0.25 * rx2

    glBegin(GL_POINTS)

    # -------- Region 1 --------
    while 2 * ry2 * x < 2 * rx2 * y:
        plot_ellipse_points(xc, yc, x, y)
        if p1 < 0:
            x += 1
            p1 += 2 * ry2 * x + ry2
        else:
            x += 1
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2

    # Region 2 decision parameter
    p2 = ry2 * (x + 0.5) ** 2 + rx2 * (y - 1) ** 2 - rx2 * ry2

    # -------- Region 2 --------
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)
        if p2 > 0:
            y -= 1
            p2 -= 2 * rx2 * y + rx2
        else:
            x += 1
            y -= 1
            p2 += 2 * ry2 * x - 2 * rx2 * y + rx2

    glEnd()

# ---------------- OpenGL Setup ----------------
def init():
    glClearColor(0, 0, 0, 1)
    glColor3f(1, 1, 1)
    gluOrtho2D(0, 500, 0, 500)

# ---------------- Main Program ----------------
def main():
    pygame.init()
    pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Midpoint Ellipse Algorithm")
    init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)
        midpoint_ellipse(250, 250, 150, 100)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
