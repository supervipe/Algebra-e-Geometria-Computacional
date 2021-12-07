import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

from shape2d import *
from shape3d import *
from grafo import *

if __name__ == "__main__":
    pygame.init()
    display = (1000, 1000)
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
    usaC = Line3d([1.5, 1, 1.5], [1, 1.5, 1.5])
    usaP = Line3d([1.5, 1, 1.5], [2, 0.7, -0.2])
    argentinaAus = Line3d([1.3, -1.2, 1.5], [0.3, -1, -2.1])
    canadaR = Line3d([1, 1.5, 1.5], [1.5, 1.2, -1.5])
    canadaP = Line3d([1, 1.5, 1.5], [2, 0.7, -0.2])
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
    russiaP = Line3d([1.5, 1.2, -1.5], [2, 0.7, -0.2])


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
    x = 0
    uColor = 0
    cColor = 0
    afriColor = 0
    bColor = 0
    arColor = 0
    eColor = 0
    pColor = 0
    iColor = 0
    rColor = 0
    ausColor = 0
    jColor = 0
    buColor = 0
    barColor = 0
    bafColor = 0
    ucColor = 0
    cpColor = 0
    upColor = 0
    aaColor = 0
    crColor = 0
    rpColor = 0
    prColor = 0
    peColor = 0
    epColor = 0
    aeColor = 0
    eiColor = 0
    ijColor = 0
    iaColor = 0
    aiColor = 0
    ajColor = 0
    rjColor = 0
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


        sphere.draw(0.1, 0.5, 0.1)
        usa.draw(0.2 + uColor, 0.2 + uColor, 0.8 - uColor)
        canada.draw(0.2 + cColor, 0.2 + cColor, 0.8 - cColor)
        brasil.draw(0.2 + bColor, 0.2 + bColor, 0.8 - bColor)
        argentina.draw(0.2 + arColor, 0.2 + arColor, 0.8 - arColor)
        africaSul.draw(0.2 + afriColor, 0.2 + afriColor, 0.8 - afriColor) 
        egito.draw(0.2 + eColor, 0.2 + eColor, 0.8 - eColor)
        portugal.draw(0.2 + pColor, 0.2 + pColor, 0.8 - pColor)
        india.draw(0.2 + iColor, 0.2 + iColor, 0.8 - iColor)
        russia.draw(0.2 + rColor, 0.2 + rColor, 0.8 - rColor)
        australia.draw(0.2 + ausColor, 0.2 + ausColor, 0.8 - ausColor)
        japao.draw(0.2 + jColor, 0.2 + jColor, 0.8 - jColor)
        
        brasilUsa.draw(0.5 + buColor, 0.2 + buColor, 0.8 - buColor)
        brasilArgentina.draw(0.5 + barColor, 0.2 + barColor, 0.8 - barColor)
        brasilAfricaSul.draw(0.5 + bafColor, 0.2 + bafColor, 0.8 - bafColor)
        usaC.draw(0.5 + ucColor, 0.2 + ucColor, 0.8 - ucColor)
        usaP.draw(0.5 + upColor, 0.2 + upColor, 0.8 - upColor)
        argentinaAus.draw(0.5 + aaColor, 0.2 + aaColor, 0.8 - aaColor)
        canadaR.draw(0.5 + crColor, 0.2 + crColor, 0.8 - crColor)
        canadaP.draw(0.5 + cpColor, 0.2 + cpColor, 0.8 - cpColor)
        portugalR.draw(0.5 + prColor, 0.2 + prColor, 0.8 - prColor)
        portugalE.draw(0.5 + peColor, 0.2 + peColor, 0.8 - peColor)
        egitoP.draw(0.5 + epColor, 0.2 + epColor, 0.8 - epColor)
        africaSulE.draw(0.5 + aeColor, 0.2 + aeColor, 0.8 - aeColor)
        egitoI.draw(0.5 + eiColor, 0.2 + eiColor, 0.8 - eiColor)
        indiaJ.draw(0.5 + ijColor, 0.2 + ijColor, 0.8 - ijColor)
        indiaAustralia.draw(0.5 + iaColor, 0.2 + iaColor, 0.8 - iaColor)
        australiaI.draw(0.5 + aiColor, 0.2 + aiColor, 0.8 - aiColor)
        australiaJ.draw(0.5 + ajColor, 0.2 + ajColor, 0.8 - ajColor)
        russiaJ.draw(0.5 + rjColor, 0.2 + rjColor, 0.8 - rjColor)
        russiaP.draw(0.5 + rpColor, 0.2 + rpColor, 0.8 - rpColor)

        valor, ini, fim = fluxoMaximo()
        print(ini)
        # for x in range(len(ini) - 1):
        if ini[x] == "brasil":
            bColor = 1
            if fim[x] == "usa":
                buColor = 0.5
                uColor = 0.5
            elif fim[x] == "africaSul":
                bafColor = 0.5
                afriColor = 0.5
            elif fim[x] == "argentina":
                barColor = 0.5
                arColor = 0.5
        if ini[x] == "usa":
            uColor = 1
            if fim[x] == "canada":
                ucColor = 0.5
                cColor = 0.5
            elif fim[x] == "portugal":
                upColor = 0.5
                pColor = 0.5 
        if ini[x] == "canada":
            cColor = 1
            if fim[x] == "portugal":
                cpColor = 0.5
                pColor = 0.5
            elif fim[x] == "russia":
                crColor = 0.5
                rColor = 0.5
        if ini[x] == "russia":
            rColor = 1
            if fim[x] == "portugal":
                rpColor = 0.5
                pColor = 0.5
            elif fim[x] == "japao":
                rjColor = 0.5
                jColor = 0.5
        if ini[x] == "portugal":
            pColor = 1
            if fim[x] == "egito":
                epColor = 0.5
                eColor = 0.5
            elif fim[x] == "russia":
                prColor = 0.5
                rColor = 0.5
        if ini[x] == "argentina":
            arColor = 1
            if fim[x] == "australia":
                aaColor = 0.5
                ausColor = 0.5
        if ini[x] == "africaSul":
            afriColor = 1
            if fim[x] == "egito":
                aeColor = 0.5
                eColor = 0.5
        if ini[x] == "egito":
            eColor = 1
            if fim[x] == "india":
                eiColor = 0.5
                iColor = 0.5
        if ini[x] == "india":
            iColor = 1
            if fim[x] == "japao":
                jColor = 0.5
            elif fim[x] == "australia":
                ausColor = 0.5
        if ini[x] == "australia":
            ausColor = 1
            if fim[x] == "india":
                aiColor = 0.5
                iColor = 0.5
            elif fim[x] == "japao":
                ajColor = 0.5
                jColor = 0.5
        
        if(len(ini)-1 != x):
            x = x + 1

        pygame.display.flip()
        pygame.time.wait(1500)
