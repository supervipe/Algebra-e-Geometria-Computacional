import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

from shape2d import *
from shape3d import *

if __name__ == "__main__":
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(80, display[0]/display[1], 0.1, 50.0)
    glTranslate(0.0, 0.0, -5)

    square = Square(1, 1, 1)
    rectangle = Rectangle(1, 1, 2, 1)
    triangle = Triangle([1, 0], [0, 0], [0, 1])
    line = Line([1, 0], [3, 0])
    circle = Circle(0, 0, 1, 80)

    cube = Cube(1, 2, 1, 1)
    parallelepiped = Parallelepiped(1, 1, 1, 1, 1, 2)
    piramid = Piramid(0, 1, 0, 1, 1, 1.5)
    line3d = Line3d([0, 1, 1], [2, 2, 2])
    sphere = Sphere(1, 1, 1, 1, 10, 10)

    # square.projectionX2D()
    # square.projectionY2D()
    # square.reflectX2D()
    # square.reflectY2D()
    # square.rotate2D(45)
    # square.shear(45)
    # square.translate2D(1, -1)
    # square.scaleX2D(2)
    # square.scaleY2D(2)

    # sphere.projectionXZ3D()
    # sphere.projectionYX3D()
    # sphere.projectionZY3D()
    # sphere.reflectX3D()
    # sphere.reflectY3D()
    # sphere.reflectZ3D()
    # sphere.rotateX3D(45)
    # sphere.rotateY3D(45)
    # sphere.rotateZ3D(45)
    # sphere.scaleX3D(2)
    # sphere.scaleY3D(2)
    # sphere.scaleZ3D(2)
    sphere.translate3D(-1, 2, 4)

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotate(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # square.draw()
        # rectangle.draw()
        # triangle.draw()
        # line.draw()
        # circle.draw()

        # cube.draw()
        # parallelepiped.draw()
        # piramid.draw()
        # line3d.draw()
        sphere.draw()

        pygame.display.flip()
        pygame.time.wait(10)
