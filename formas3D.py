import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from matrix import Matrix
from math import sqrt, cos, tan, sin, pi

class Cube:
    def __init__(self, x, y, z, width):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list =[]
        points_list.append([self.x, self.y, self.z])
        points_list.append([self.x, self.y + self.width, self.z])
        points_list.append([self.x + self.width, self.y + self.width, self.z])
        points_list.append([self.x + self.width, self.y, self.z])
        points_list.append([self.x, self.y, self.z + self.width])
        points_list.append([self.x, self.y + self.width, self.z + self.width])
        points_list.append([self.x + self.width, self.y + self.width, self.z + self.width])
        points_list.append([self.x + self.width, self.y, self.z + self.width])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        for i in range(1, 3):
            glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
            glVertex3f(self.points[i][0],self.points[i][1],self.points[i][2])
            glVertex3f(self.points[i + 1][0],self.points[i +1][1],self.points[i +1][2])
        for i in range(3, 5):
            glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
            glVertex3f(self.points[7][0],self.points[7][1],self.points[7][2])
            glVertex3f(self.points[i][0],self.points[i][1],self.points[i][2])
        glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
        glVertex3f(self.points[4][0],self.points[4][1],self.points[4][2])
        glVertex3f(self.points[5][0],self.points[5][1],self.points[1][2])

        glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])
        glVertex3f(self.points[5][0],self.points[5][1],self.points[5][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[4][0],self.points[4][1],self.points[4][2])
        glVertex3f(self.points[5][0],self.points[5][1],self.points[5][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[4][0],self.points[4][1],self.points[4][2])
        glVertex3f(self.points[7][0],self.points[7][1],self.points[7][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])
        glVertex3f(self.points[2][0],self.points[2][1],self.points[2][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])
        glVertex3f(self.points[5][0],self.points[5][1],self.points[5][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[3][0],self.points[3][1],self.points[3][2])
        glVertex3f(self.points[2][0],self.points[2][1],self.points[2][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[3][0],self.points[3][1],self.points[3][2])
        glVertex3f(self.points[7][0],self.points[7][1],self.points[7][2])

        glEnd()

class Para:
    def __init__(self, x, y, z, width, height, length):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.length = length
        self.points = self._create_points()

    def _create_points(self):
        points_list =[]
        points_list.append([self.x, self.y, self.z])
        points_list.append([self.x, self.y + self.height, self.z])
        points_list.append([self.x + self.length, self.y + self.height, self.z])
        points_list.append([self.x + self.length, self.y, self.z])
        points_list.append([self.x, self.y, self.z + self.width])
        points_list.append([self.x, self.y + self.height, self.z + self.width])
        points_list.append([self.x + self.length, self.y + self.height, self.z + self.width])
        points_list.append([self.x + self.length, self.y, self.z + self.width])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        for i in range(1, 3):
            glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
            glVertex3f(self.points[i][0],self.points[i][1],self.points[i][2])
            glVertex3f(self.points[i + 1][0],self.points[i +1][1],self.points[i +1][2])
        for i in range(3, 5):
            glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
            glVertex3f(self.points[7][0],self.points[7][1],self.points[7][2])
            glVertex3f(self.points[i][0],self.points[i][1],self.points[i][2])
        glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
        glVertex3f(self.points[4][0],self.points[4][1],self.points[4][2])
        glVertex3f(self.points[5][0],self.points[5][1],self.points[1][2])

        glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])
        glVertex3f(self.points[5][0],self.points[5][1],self.points[5][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[4][0],self.points[4][1],self.points[4][2])
        glVertex3f(self.points[5][0],self.points[5][1],self.points[5][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[4][0],self.points[4][1],self.points[4][2])
        glVertex3f(self.points[7][0],self.points[7][1],self.points[7][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])
        glVertex3f(self.points[2][0],self.points[2][1],self.points[2][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])
        glVertex3f(self.points[5][0],self.points[5][1],self.points[5][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[3][0],self.points[3][1],self.points[3][2])
        glVertex3f(self.points[2][0],self.points[2][1],self.points[2][2])

        glVertex3f(self.points[6][0],self.points[6][1],self.points[6][2])
        glVertex3f(self.points[3][0],self.points[3][1],self.points[3][2])
        glVertex3f(self.points[7][0],self.points[7][1],self.points[7][2])

        glEnd()
    def rotatex3D(self, ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().rotatex3D(self.points[i],ang)
        return self.points
    def rotatey3D(self, ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().rotatey3D(self.points[i],ang)
        return self.points
    def rotatez3D(self, ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().rotatez3D(self.points[i],ang)
        return self.points
    def projxz3D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projxz3D(self.points[i])
        return self.points
    def projyx3D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projyx3D(self.points[i])
        return self.points
    def projzy3D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().projzy3D(self.points[i])
        return self.points
    def cisalhamento3D(self,ang):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().cisalhamento3D(self.points[i],ang)
        return self.points
    def reflex3D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().reflex3D(self.points[i])
        return self.points
    def refley3D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().refley3D(self.points[i])
        return self.points
    def reflez3D(self):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().reflez3D(self.points[i])
        return self.points
    def transla3D(self,x,y,z):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().transla3D(self.points[i],x,y,z)
        return self.points
    def escalonamento3D(self,x,y,z):
        for i in range(0, len(self.points)):
            self.points[i] = Transf().escalonamento3D(self.points[i],x,y,z)
        return self.points

class Piram:
    def __init__(self, x, y, z, width, height, length):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.length = length
        self.points = self._create_points()

    def _create_points(self):
        points_list =[]
        points_list.append([self.x, self.y, self.z])
        points_list.append([self.x - self.length/2 , self.y - self.height, self.z + self.width/2])
        points_list.append([self.x - self.length/2 , self.y - self.height, self.z - self.width/2])
        points_list.append([self.x + self.length/2 , self.y - self.height, self.z + self.width/2])
        points_list.append([self.x + self.length/2 , self.y - self.height, self.z - self.width/2])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(0.0, 1.0,0.0)
        glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])
        glVertex3f(self.points[2][0],self.points[2][1],self.points[2][2])

        glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
        glVertex3f(self.points[3][0],self.points[3][1],self.points[3][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])

        glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
        glVertex3f(self.points[3][0],self.points[3][1],self.points[3][2])
        glVertex3f(self.points[4][0],self.points[4][1],self.points[4][2])

        glVertex3f(self.points[0][0],self.points[0][1],self.points[0][2])
        glVertex3f(self.points[2][0],self.points[2][1],self.points[2][2])
        glVertex3f(self.points[4][0],self.points[4][1],self.points[4][2])

        glVertex3f(self.points[3][0],self.points[3][1],self.points[3][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])
        glVertex3f(self.points[2][0],self.points[2][1],self.points[2][2])

        glVertex3f(self.points[3][0],self.points[3][1],self.points[3][2])
        glVertex3f(self.points[1][0],self.points[1][1],self.points[1][2])
        glVertex3f(self.points[4][0],self.points[4][1],self.points[4][2])
        glEnd()

class Sphere:
    # Params:
        # x, y, z: Center coordinates
        # raius
        # sectors: Number of horizontal sections wanted ( longitudes )
        # stacks: Number of vertical sections wanted ( latitudes )
    def __init__(self, x, y, z, radius, sectors, stacks):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.sectors = sectors
        self.stacks = stacks
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        sectorStep = 2 * pi / self.sectors
        stackStep = pi / self.stacks

        for i in range(0, self.stacks + 1):
            stackAngle = pi / 2 - i * stackStep
            zx = self.radius * cos(stackAngle)
            y = self.y + self.radius * sin(stackAngle)

            for j in range(0, self.sectors + 1):
                sectorAngle = j * sectorStep
                z = self.z + (zx * cos(sectorAngle))
                x = self.x + (zx * sin(sectorAngle))
                points_list.append([x, y, z])
        return points_list

    def draw(self):

        for i in range(0, self.stacks):
            k1 = i * (self.sectors + 1)
            k2 = k1 + self.sectors + 1

            glBegin(GL_TRIANGLES)
            for j in range(0, self.sectors):

                if i != 0:
                    glColor(1.0, 0.9 - 0.04 * j, 1.0)
                    glVertex3f(
                        self.points[k1][0], self.points[k1][1], self.points[k1][2])
                    glVertex3f(
                        self.points[k2][0], self.points[k2][1], self.points[k2][2])
                    glVertex3f(
                        self.points[k1 + 1][0], self.points[k1 + 1][1], self.points[k1 + 1][2])

                if i != (self.stacks - 1):
                    glColor(1.0, 1.0,  0.9 - 0.04 * j)
                    glVertex3f(
                        self.points[k1 + 1][0], self.points[k1 + 1][1], self.points[k1 + 1][2])
                    glVertex3f(
                        self.points[k2][0], self.points[k2][1], self.points[k2][2])
                    glVertex3f(
                        self.points[k2 + 1][0], self.points[k2 + 1][1], self.points[k2 + 1][2])

                k1 = k1 + 1
                k2 = k2 + 1

            glEnd()
class Transf:
    def reflex3D(self, point):
        x,y,z = point
        dom = Matrix (3 , 1 , [x,y,z])
        k = Matrix(3,3)

        k[1,1] = 1 
        k[2,2] = -1
        k[3,3] = -1 

        dom = k.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        z = dom[3,1]
        return [x,y,z]

    def refley3D(self, point):
        x,y,z = point
        dom = Matrix (3 , 1 , [x,y,z])
        k = Matrix(3,3)

        k[1,1] = -1 
        k[2,2] = 1
        k[3,3] = -1 

        dom = k.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        z = dom[3,1]
        return [x,y,z]

    def reflez3D(self, point):
        x,y,z = point
        dom = Matrix (3 , 1 , [x,y,z])
        k = Matrix(3,3)

        k[1,1] = -1 
        k[2,2] = -1
        k[3,3] = 1 

        dom = k.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        z = dom[3,1]
        return [x,y,z]


    def projxz3D(self, point):
        x,y,z = point
        dom = Matrix(3, 1, [x,y,z])
        k = Matrix(3,3)

        k[1,1] = 1
        k[2,2] = 0
        k[3,3] = 1

        dom = k.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        z = dom[3,1]
        return [x,y,z]

    def projyx3D(self, point):
        x,y,z = point
        dom = Matrix(3, 1, [x,y,z])
        k = Matrix(3,3)

        k[1,1] = 1
        k[2,2] = 1
        k[3,3] = 0

        dom = k.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        z = dom[3,1] 
        return [x,y,z]

    def projzy3D(self, point):
        x,y,z = point
        dom = Matrix(3, 1, [x,y,z])
        k = Matrix(3,3)

        k[1,1] = 0
        k[2,2] = 1
        k[3,3] = 1

        dom = k.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        z = dom[3,1] 
        return [x,y,z]

    def rotatex3D(self, point,ang):
        ang = ang * pi / 180
        x,y,z = point
        dom = Matrix(3, 1, [x,y,z])
        k = Matrix(3,3)

        k[1,1] = 1
        k[2,2] = cos(ang)
        k[2,3] = -sin(ang)
        k[3,2] = sin(ang)
        k[3,3] = cos(ang)

        dom = k.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        z = dom[3,1] 
        return [x,y,z]

    def rotatey3D(self, point,ang):
        ang = ang * pi / 180
        x,y,z = point
        dom = Matrix(3, 1, [x,y,z])
        k = Matrix(3,3)

        k[1,1] = cos(ang)
        k[1,3] = sin(ang) 
        k[3,1] = -sin(ang) 
        k[2,2] = 1
        k[3,3] = cos(ang)

        dom = k.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        z = dom[3,1] 
        return [x,y,z]


    def rotatez3D(self, point,ang):
        ang = ang * pi / 180
        x,y,z = point
        dom = Matrix(3, 1, [x,y,z])
        k = Matrix(3,3)

        k[1,1] = cos(ang)
        k[1,2] = -sin(ang) 
        k[2,1] = sin(ang) 
        k[2,2] = cos(ang)
        k[3,3] = 1

        dom = k.dot(dom)
        x = dom[1,1] #
        y = dom[2,1] #
        z = dom[3,1] #
        return [x,y,z]

    def escalonamento3D(self, point, x, y, z):
        xp,yp,zp = point
        dom = Matrix(3, 1, [xp,yp,zp])
        k = Matrix(3, 3)
        k[1,1] = x
        k[2,2] = y
        k[3,3] = z

        dom = k.dot(dom)
        xp = dom[1,1]
        yp = dom[2,1]
        zp = dom[3,1]
        return [xp,yp,zp]

    def cisalhamento3D(self,point, ang):
        ang = ang * pi / 180
        x,y,z = point
        dom = Matrix(3, 1, [x,y,z])
        k = Matrix(3,3)
        k[1,2] = tan(ang)
        k[1,1] = 1
        k[2,2] = 1
        k[3,3] = 1

        dom = k.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        z = dom[3,1]
        return [x,y,z]

    def transla3D(self, point,x,y,z):
        xp, yp, zp = point
        dom = Matrix(3, 1, [xp,yp,zp])
        k = Matrix(3, 3)

        k[1,1] = 1
        k[2,2] = 1
        k[3,3] = 1

        dom = k.dot(dom)
        xp = dom[1,1] + x
        yp = dom[2,1] + y
        zp = dom[3,1] + z
        return [xp,yp,zp]


if __name__ == "__main__":
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glTranslate(0.0, 0.0, -10)

    square = Para(0,0,0, 1,3,2)
    square.projyx3D()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotate(1,0,1,0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        square.draw()
        pygame.display.flip()
        pygame.time.wait(10)
