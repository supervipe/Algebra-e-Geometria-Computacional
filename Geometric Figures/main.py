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

    # square = Square(1, 1, 1)
    # rectangle = Rectangle(1, 1, 2, 1)
    # triangle = Triangle([1, 0], [0, 0], [0, 1])
    # line = Line([1, 0], [3, 0])
    # circle = Circle(0, 0, 1, 80)

    # cube = Cube(1, 2, 1, 1)
    # parallelepiped = Parallelepiped(1, 1, 1, 1, 1, 2)
    # piramid = Piramid(0, 1, 0, 1, 1, 1.5)
    brasilUsa = Line3d([1.7, -0.5, 1.9], [1.5, 1, 1.5])
    brasilArgentina = Line3d([1.7, -0.5, 1.9], [1.3, -1.2, 1.5])
    brasilAfricaSul = Line3d([1.7, -0.5, 1.9], [1.9, -1.3, -0.8])
    usaC = Line3d([1, 1.5, 1.5], [1.5, 1, 1.5])
    usaP = Line3d([1, 1.5, 1.5], [2, 0.7, -0.2])
    argentinaAus = Line3d([1.3, -1.2, 1.5], [0.3, -1, -2.1])
    canadaR = Line3d([1, 1.5, 1.5], [1.5, 1.2, -1.5])
    portugalR = Line3d([2, 0.7, -0.2], [1.5, 1.2, -1.5])
    portugalE = Line3d([2, 0.7, -0.2], [2.2, 0, -0.8])
    egitoP = Line3d([2.2, 0, -0.8], [2, 0.7, -0.2])
    africaSulE = Line3d([1.9, -1.3, -0.8], [2.2, 0, -0.8])
    egitoI = Line3d([2.2, 0, -0.8], [1.3, -0.4, -1.8])
    indiaJ = Line3d([1.3, -0.4, -1.8], [0, 0, -2.2])
    indiaAustralia = Line3d([1.3, -0.4, -1.8], [0.3, -1, -2.1])
    australiaI = Line3d([0.3, -1, -2.1], [1.3, -0.4, -1.8])
    australiaJ = Line3d([0.3, -1, -2.1], [0, 0, -2.2])
    russiaJ = Line3d([1.5, 1.2, -1.5], [0, 0, -2.2])


    sphere = Sphere(0, 0, 0, 2, 50, 50)
    usa = Sphere(1.5, 1, 1.5, 0.05, 50, 50)
    canada = Sphere(1, 1.5, 1.5, 0.05, 50, 50)
    brasil = Sphere(1.7, -0.5, 1.9, 0.05, 50, 50)
    argentina = Sphere(1.3, -1.2, 1.5, 0.05, 50, 50)
    africaSul = Sphere(1.9, -1.3, -0.8, 0.05, 50, 50)
    egito = Sphere(2.2, 0, -0.8, 0.05, 50, 50)
    portugal = Sphere(2, 0.7, -0.2, 0.05, 50, 50)
    india = Sphere(1.3, -0.4, -1.8, 0.05, 50, 50)
    russia = Sphere(1.5, 1.2, -1.5, 0.05, 50, 50)
    australia = Sphere(0.3, -1, -2.1, 0.05, 50, 50)
    japao = Sphere(0, 0, -2.2, 0.05, 50, 50)

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - display[i] for i in range(2)]
                glRotatef(mouseMove[0]*0.01, 0.0, 1.0, 0.0)

        # glRotate(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        sphere.draw()
        usa.draw()
        canada.draw()
        brasil.draw()
        argentina.draw()
        africaSul.draw()
        egito.draw()
        portugal.draw()
        india.draw()
        russia.draw()
        australia.draw()
        japao.draw()
        
        brasilUsa.draw()
        brasilArgentina.draw()
        brasilAfricaSul.draw()
        usaC.draw()
        usaP.draw()
        argentinaAus.draw()
        canadaR.draw()
        portugalR.draw()
        portugalE.draw()
        egitoP.draw()
        africaSulE.draw()
        egitoI.draw()
        indiaJ.draw()
        indiaAustralia.draw()
        australiaI.draw()
        australiaJ.draw()
        russiaJ.draw()


        pygame.display.flip()
        pygame.time.wait(80)
