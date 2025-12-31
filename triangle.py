import pygame as pg
from OpenGL.GL import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((800, 600), pg.OPENGL | pg.DOUBLEBUF)

        # Background color (R,G,B,A)
        glClearColor(0.1, 0.1, 0.1, 1)

        self.running = True

    def draw_triangle(self):
        glBegin(GL_TRIANGLES)

        glColor3f(1, 0, 0)     # Red
        glVertex2f(-0.5, -0.5)

        glColor3f(0, 1, 0)     # Green
        glVertex2f(0.5, -0.5)

        glColor3f(0, 0, 1)     # Blue
        glVertex2f(0, 0.5)

        glEnd()

    def mainloop(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            glClear(GL_COLOR_BUFFER_BIT)

            self.draw_triangle()   # Draw triangle here

            pg.display.flip()

        pg.quit()

if __name__ == "__main__":
    App().mainloop()
