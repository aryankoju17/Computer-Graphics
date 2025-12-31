from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import random
import math

# ---------------- OpenGL Initialization ----------------
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    gluOrtho2D(0, 500, 0, 500)        # 2D coordinate system

# ---------------- Pie Chart Drawing ----------------
def draw_pie_chart(cx, cy, r, angles, slice_colors, steps=100):
    # Draw each slice using precomputed angles and fixed colors
    for i, (start, end) in enumerate(angles):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(*slice_colors[i])  # Fixed color for this slice
        glVertex2f(cx, cy)           # Center point
        for k in range(steps + 1):
            theta = math.radians(start + k * (end - start) / steps)
            x = cx + r * math.cos(theta)
            y = cy + r * math.sin(theta)
            glVertex2f(x, y)
        glEnd()

# ---------------- Main Program ----------------
def main():
    pygame.init()
    pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Pie Chart")
    init()

    # ----- Parameters -----
    n_slices = 6
    cx, cy = 250, 250
    r = 150
    steps = 100

    # ----- Generate slice values once -----
    slice_values = [random.randint(5, 50) for _ in range(n_slices)]
    total = sum(slice_values)

    # ----- Compute start and end angles once -----
    angles = []
    start_angle = 0
    for value in slice_values:
        angle_i = 360 * value / total
        end_angle = start_angle + angle_i
        angles.append((start_angle, end_angle))
        start_angle = end_angle

    # ----- Assign fixed colors -----
    colors = [
        (1, 0, 0),   # Red
        (0, 1, 0),   # Green
        (0, 0, 1),   # Blue
        (1, 1, 0),   # Yellow
        (1, 0, 1),   # Magenta
        (0, 1, 1),   # Cyan
    ]

    # ----- Main Loop -----
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)
        draw_pie_chart(cx, cy, r, angles, colors, steps)
        pygame.display.flip()
        pygame.time.wait(50)

    pygame.quit()

if __name__ == "__main__":
    main()
