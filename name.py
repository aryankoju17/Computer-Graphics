# import glfw
# from OpenGL.GL import *

# def draw_rect(x, y, width, height):
#     """Helper to draw a filled rectangle (polygon)"""
#     glBegin(GL_POLYGON)
#     glVertex2f(x, y)
#     glVertex2f(x + width, y)
#     glVertex2f(x + width, y + height)
#     glVertex2f(x, y + height)
#     glEnd()

# def draw_name():
#     # Set color to Pink (R=1.0, G=0.75, B=0.8)
#     glColor3f(1.0, 0.75, 0.8)

#     # --- Letter A (First) ---
#     glBegin(GL_POLYGON) # Left Leg
#     glVertex2f(-0.8, -0.3); glVertex2f(-0.7, -0.3); glVertex2f(-0.6, 0.3); glVertex2f(-0.7, 0.3)
#     glEnd()
#     glBegin(GL_POLYGON) # Right Leg
#     glVertex2f(-0.6, 0.3); glVertex2f(-0.5, 0.3); glVertex2f(-0.4, -0.3); glVertex2f(-0.5, -0.3)
#     glEnd()
#     draw_rect(-0.7, -0.05, 0.2, 0.05) # Bar

#     # --- Letter R ---
#     draw_rect(-0.3, -0.3, 0.08, 0.6) # Vertical Stem
#     draw_rect(-0.22, 0.25, 0.15, 0.05) # Top Bar
#     draw_rect(-0.22, 0.0, 0.15, 0.05)  # Middle Bar
#     draw_rect(-0.07, 0.0, 0.05, 0.3)   # Right side of loop
#     glBegin(GL_POLYGON) # Slanted Leg
#     glVertex2f(-0.22, 0.0); glVertex2f(-0.12, 0.0); glVertex2f(0.0, -0.3); glVertex2f(-0.1, -0.3)
#     glEnd()

#     # --- Letter Y ---
#     draw_rect(0.2, -0.3, 0.08, 0.3) # Stem
#     glBegin(GL_POLYGON) # Left Branch
#     glVertex2f(0.1, 0.3); glVertex2f(0.18, 0.3); glVertex2f(0.24, 0.0); glVertex2f(0.16, 0.0)
#     glEnd()
#     glBegin(GL_POLYGON) # Right Branch
#     glVertex2f(0.38, 0.3); glVertex2f(0.3, 0.3); glVertex2f(0.24, 0.0); glVertex2f(0.32, 0.0)
#     glEnd()

#     # --- Letter A (Second) ---
#     glBegin(GL_POLYGON) # Left Leg
#     glVertex2f(0.45, -0.3); glVertex2f(0.55, -0.3); glVertex2f(0.65, 0.3); glVertex2f(0.55, 0.3)
#     glEnd()
#     glBegin(GL_POLYGON) # Right Leg
#     glVertex2f(0.65, 0.3); glVertex2f(0.75, 0.3); glVertex2f(0.85, -0.3); glVertex2f(0.75, -0.3)
#     glEnd()
#     draw_rect(0.58, -0.05, 0.15, 0.05) # Bar

#     # --- Letter N ---
#     draw_rect(0.9, -0.3, 0.07, 0.6)  # Left Vertical
#     draw_rect(1.15, -0.3, 0.07, 0.6) # Right Vertical
#     # Diagonal: connect inner top edge of left bar to inner bottom edge of right bar
#     glBegin(GL_POLYGON)
#     glVertex2f(0.97, 0.3); glVertex2f(1.03, 0.3); glVertex2f(1.15, -0.3); glVertex2f(1.09, -0.3)
#     glEnd()

# def main():
#     if not glfw.init():
#         return

#     # Window adjusted for the wider name
#     window = glfw.create_window(1200, 600, "Name: ARYAN", None, None)
#     if not window:
#         glfw.terminate()
#         return

#     glfw.make_context_current(window)

#     while not glfw.window_should_close(window):
#         # Set background to a dark grey to make the pink pop
#         glClearColor(0.1, 0.1, 0.1, 1.0)
#         glClear(GL_COLOR_BUFFER_BIT)

#         draw_name()

#         glfw.swap_buffers(window)
#         glfw.poll_events()

#     glfw.terminate()

# if __name__ == "__main__":
#     main()

import glfw
from OpenGL.GL import *

def draw_rect(x, y, width, height):
    """Helper to draw a filled rectangle (polygon)"""
    glBegin(GL_POLYGON)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def draw_name():
    # Set color to Pink
    glColor3f(1.0, 0.75, 0.8)

    # --- Letter A (First) ---
    glBegin(GL_POLYGON) # Left Leg
    glVertex2f(-0.8, -0.3); glVertex2f(-0.7, -0.3); glVertex2f(-0.65, 0.3); glVertex2f(-0.75, 0.3)
    glEnd()
    glBegin(GL_POLYGON) # Right Leg
    glVertex2f(-0.65, 0.3); glVertex2f(-0.55, 0.3); glVertex2f(-0.45, -0.3); glVertex2f(-0.55, -0.3)
    glEnd()
    draw_rect(-0.7, -0.05, 0.15, 0.05)

    # --- Letter R ---
    draw_rect(-0.35, -0.3, 0.08, 0.6) 
    draw_rect(-0.27, 0.25, 0.15, 0.05) 
    draw_rect(-0.27, 0.0, 0.15, 0.05)  
    draw_rect(-0.12, 0.0, 0.05, 0.3)   
    glBegin(GL_POLYGON) # Slanted Leg
    glVertex2f(-0.27, 0.0); glVertex2f(-0.17, 0.0); glVertex2f(-0.05, -0.3); glVertex2f(-0.15, -0.3)
    glEnd()

    # --- Letter Y ---
    draw_rect(0.1, -0.3, 0.08, 0.3) 
    glBegin(GL_POLYGON) # Left Branch
    glVertex2f(0.0, 0.3); glVertex2f(0.08, 0.3); glVertex2f(0.14, 0.0); glVertex2f(0.06, 0.0)
    glEnd()
    glBegin(GL_POLYGON) # Right Branch
    glVertex2f(0.28, 0.3); glVertex2f(0.2, 0.3); glVertex2f(0.14, 0.0); glVertex2f(0.22, 0.0)
    glEnd()

    # --- Letter A (Second) ---
    glBegin(GL_POLYGON) # Left Leg
    glVertex2f(0.3, -0.3); glVertex2f(0.4, -0.3); glVertex2f(0.45, 0.3); glVertex2f(0.35, 0.3)
    glEnd()
    glBegin(GL_POLYGON) # Right Leg
    glVertex2f(0.45, 0.3); glVertex2f(0.55, 0.3); glVertex2f(0.6, -0.3); glVertex2f(0.5, -0.3)
    glEnd()
    draw_rect(0.4, -0.05, 0.15, 0.05)

   # --- Letter N ---
    draw_rect(0.7, -0.3, 0.07, 0.6)  # Left Vertical
    draw_rect(0.9, -0.3, 0.07, 0.6)  # Right Vertical
    glBegin(GL_POLYGON) # Diagonal
    glVertex2f(0.7, 0.3)   # Top-left of diagonal
    glVertex2f(0.8, 0.3)   # Top-right of diagonal
    glVertex2f(0.97, -0.3) # Bottom-right of diagonal
    glVertex2f(0.87, -0.3) # Bottom-left of diagonal
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(2000, 1000, "Name: ARYAN", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClearColor(0.1, 0.1, 0.1, 1.0) # Dark background
        glClear(GL_COLOR_BUFFER_BIT)

        draw_name()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()