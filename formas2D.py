import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi,sin,cos,tan
from matrix import Matrix

class Square: 

    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list =[]
        points_list.append([self.x, self.y])
        points_list.append([self.x + self.width, self.y])
        points_list.append([self.x + self.width, self.y + self.width])
        points_list.append([self.x, self.y + self.width])
        return points_list

    def draw(self):
        if(self.points[0][1] == 0 or self.points[0][0] == 0):
            glBegin(GL_LINES)
        else:
            glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0],self.points[0][1])
        glVertex2f(self.points[1][0],self.points[1][1])
        glVertex2f(self.points[2][0],self.points[2][1])

        glVertex2f(self.points[0][0],self.points[0][1])
        glVertex2f(self.points[2][0],self.points[2][1])
        glVertex2f(self.points[3][0],self.points[3][1])
        glEnd()

    def rotate2D(self, ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().rotate2D(self.points[i],ang)
        return self.points
    def projx2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projx2D(self.points[i])
        return self.points
    def projy2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projy2D(self.points[i])
        return self.points
    def cisalhamento(self,ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().cisalhamento(self.points[i],ang)
        return self.points
    def reflex2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().reflex2D(self.points[i])
        return self.points
    def refley2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().refley2D(self.points[i])
        return self.points
    def transla2D(self,x,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().transla2D(self.points[i],x,y)
        return self.points
    def escalonamentoy2D(self,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentoy2D(self.points[i],y)
        return self.points
    def escalonamentox2D(self,x):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentox2D(self.points[i],x)
        return self.points

class Retan:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.points = self._create_points()

    def _create_points(self):
        points_list =[]
        points_list.append([self.x, self.y])
        points_list.append([self.x + self.width, self.y])
        points_list.append([self.x + self.width, self.y + self.height])
        points_list.append([self.x, self.y + self.height])
        return points_list

    def draw(self):
        if(self.points[0][1] == 0 or self.points[0][0] == 0):
            glBegin(GL_LINES)
        else:
            glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0],self.points[0][1])
        glVertex2f(self.points[1][0],self.points[1][1])
        glVertex2f(self.points[2][0],self.points[2][1])

        glVertex2f(self.points[0][0],self.points[0][1])
        glVertex2f(self.points[2][0],self.points[2][1])
        glVertex2f(self.points[3][0],self.points[3][1])
        glEnd()

    def rotate2D(self, ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().rotate2D(self.points[i],ang)
        return self.points
    def projx2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projx2D(self.points[i])
        return self.points
    def projy2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projy2D(self.points[i])
        return self.points
    def cisalhamento(self,ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().cisalhamento(self.points[i],ang)
        return self.points
    def reflex2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().reflex2D(self.points[i])
        return self.points
    def refley2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().refley2D(self.points[i])
        return self.points
    def transla2D(self,x,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().transla2D(self.points[i],x,y)
        return self.points
    def escalonamentoy2D(self,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentoy2D(self.points[i],y)
        return self.points
    def escalonamentox2D(self,x):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentox2D(self.points[i],x)
        return self.points

class Trian:
    def __init__(self, x1, y1, x2, y2,x3,y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = y2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.points = self._create_points()

    def _create_points(self):
        points_list =[]
        points_list.append([self.x1, self.y1])
        points_list.append([self.x2, self.y2])
        points_list.append([self.x3, self.y3])
        return points_list

    def draw(self):
        if(self.points[0][1] == 0 or self.points[0][0] == 0):
            glBegin(GL_LINES)
        else:
            glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0],self.points[0][1])
        glVertex2f(self.points[1][0],self.points[1][1])
        glVertex2f(self.points[2][0],self.points[2][1])

        glEnd()

    def rotate2D(self, ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().rotate2D(self.points[i],ang)
        return self.points
    def projx2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projx2D(self.points[i])
        return self.points
    def projy2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projy2D(self.points[i])
        return self.points
    def cisalhamento(self,ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().cisalhamento(self.points[i],ang)
        return self.points
    def reflex2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().reflex2D(self.points[i])
        return self.points
    def refley2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().refley2D(self.points[i])
        return self.points
    def transla2D(self,x,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().transla2D(self.points[i],x,y)
        return self.points
    def escalonamentoy2D(self,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentoy2D(self.points[i],y)
        return self.points
    def escalonamentox2D(self,x):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentox2D(self.points[i],x)
        return self.points


class Line:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list =[]
        points_list.append([self.x, self.y])
        points_list.append([self.x + self.width, self.y + self.width])
        return points_list

    def draw(self):
        glBegin(GL_LINES)
        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0],self.points[0][1])
        glVertex2f(self.points[1][0],self.points[1][1])

        glEnd()

    def rotate2D(self, ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().rotate2D(self.points[i],ang)
        return self.points
    def projx2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projx2D(self.points[i])
        return self.points
    def projy2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projy2D(self.points[i])
        return self.points
    def cisalhamento(self,ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().cisalhamento(self.points[i],ang)
        return self.points
    def reflex2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().reflex2D(self.points[i])
        return self.points
    def refley2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().refley2D(self.points[i])
        return self.points
    def transla2D(self,x,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().transla2D(self.points[i],x,y)
        return self.points
    def escalonamentoy2D(self,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentoy2D(self.points[i],y)
        return self.points
    def escalonamentox2D(self,x):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentox2D(self.points[i],x)
        return self.points

class Circle:
    def __init__(self, x, y, raio, setores):
        self.x = x
        self.y = y
        self.raio = raio
        self.setores = setores
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        ang = pi * 2 / self.setores
        for i in range(0, self.setores):
            points_list.append([self.x + (self.raio * cos(i *  ang)), self.y + (self.raio * sin(i * ang))])
        return points_list

    def draw(self):
        if(self.points[1][1] == 0 or self.points[1][0] == 0):
            glBegin(GL_LINES)
        else:
            glBegin(GL_TRIANGLES)

        for i in range(0, self.setores):
            if(i == (self.setores -1)):
                glVertex2f(self.x, self.y)
                glVertex2f(self.points[i][0],self.points[i][1])
                glVertex2f(self.points[0][0],self.points[0][1])
            else:
                glVertex2f(self.x, self.y)
                glVertex2f(self.points[i][0],self.points[i][1])
                glVertex2f(self.points[i + 1][0],self.points[i +1][1])
        glEnd()
    
    def rotate2D(self, ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().rotate2D(self.points[i],ang)
        return self.points
    def projx2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projx2D(self.points[i])
        return self.points
    def projy2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projy2D(self.points[i])
        return self.points
    def cisalhamento(self,ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().cisalhamento(self.points[i],ang)
        return self.points
    def reflex2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().reflex2D(self.points[i])
        return self.points
    def refley2D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().refley2D(self.points[i])
        return self.points
    def transla2D(self,x,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().transla2D(self.points[i],x,y)
        return self.points
    def escalonamentoy2D(self,y):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentoy2D(self.points[i],y)
        return self.points
    def escalonamentox2D(self,x):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamentox2D(self.points[i],x)
        return self.points



class Transf:
    def reflex2D(self, point):
        x,y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        
        z[1,1] = 1
        z[2,2] = -1

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]
    
    def refley2D(self, point):
        x,y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        
        z[1,1] = -1
        z[2,2] = 1

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]

    def projx2D(self, point):
        x, y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        
        z[1,1] = 1
        z[2,2] = 0

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]
    
    def projy2D(self, point):
        x,y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        
        z[1,1] = 0
        z[2,2] = 1

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]
    
    def transla2D(self, point,x,y):
        xp, yp = point
        dom = Matrix(3, 1, [xp,yp, 1])
        z = Matrix(3, 3)
        
        z[1,1] = 1
        z[2,2] = 1
        z[1,3] = x
        z[2,3] = y
        z[3,3] = 1

        dom = z.dot(dom)
        xp = dom[1,1]
        yp = dom[2,1]
        return [xp,yp]

    def cisalhamento(self,point, ang):
        ang = ang * pi / 180
        x,y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        z[1,2] = tan(ang)
        z[1,1] = 1
        z[2,2] = 1

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]

    def rotate2D(self, point, ang):
        x,y = point
        ang = ang * pi / 180
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        z[1,1] = cos(ang)
        z[1,2] = -sin(ang)
        z[2,1] = sin(ang)
        z[2,2] = cos(ang)

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]

    def escalonamentox2D(self, point, x):
        xp,yp = point
        dom = Matrix(2, 1, [xp,yp])
        z = Matrix(2, 2)
        z[1,1] = x
        z[2,2] = 1

        dom = z.dot(dom)
        xp = dom[1,1]
        yp = dom[2,1]
        return [xp,yp]

    def escalonamentoy2D(self, point, y):
        xp,yp = point
        dom = Matrix(2, 1, [xp,yp])
        z = Matrix(2, 2)
        z[1,1] = 1
        z[2,2] = y

        dom = z.dot(dom)
        xp = dom[1,1]
        yp = dom[2,1]
        return [xp,yp]

#Draw
if __name__ == "__main__":
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glTranslate(0.0, 0.0, -10)

    square = Circle(0,0, 1,50)
    square.escalonamentox2D(2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotate(1,0,1,0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        square.draw()
        pygame.display.flip()
        pygame.time.wait(10)
