import pygame as pg
from OpenGL.GL import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((800, 600), pg.OPENGL | pg.DOUBLEBUF)
        glClearColor(0, 0, 0, 1)
        self.running = True

    def draw_line(self):
        glLineWidth(3)
        glBegin(GL_LINES)

        glColor3f(1, 1, 1)
        glVertex2f(-0.7, 0)     # Start point
        glVertex2f(0.7, 0)      # End point

        glEnd()

    def mainloop(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            glClear(GL_COLOR_BUFFER_BIT)
            self.draw_line()
            pg.display.flip()

        pg.quit()

if __name__ == "__main__":
    App().mainloop()
