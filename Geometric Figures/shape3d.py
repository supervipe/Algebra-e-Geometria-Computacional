from OpenGL.GL import *
from math import sqrt, pi, cos, sin
from transform import Transform


class Cube:
    # Params:
        # x, y, z: Front-upper-left vertex coordinate
        # width: Size dimension
    def __init__(self, x, y, z, width):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y, self.z])
        points_list.append([self.x, self.y - self.width, self.z])
        points_list.append([self.x + self.width, self.y - self.width, self.z])
        points_list.append([self.x + self.width, self.y, self.z])
        points_list.append([self.x, self.y, self.z - self.width])
        points_list.append([self.x, self.y - self.width, self.z - self.width])
        points_list.append([self.x + self.width, self.y -
                            self.width, self.z - self.width])
        points_list.append([self.x + self.width, self.y, self.z - self.width])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        for i in range(1, 3):
            glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
            glVertex3f(self.points[i][0], self.points[i][1], self.points[i][2])
            glVertex3f(self.points[i + 1][0],
                       self.points[i + 1][1], self.points[i + 1][2])
        for i in range(3, 5):
            glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
            glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])
            glVertex3f(self.points[i][0], self.points[i][1], self.points[i][2])
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[1][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])

        glEnd()

    def rotateX3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateX3D(self.points[i],ang)
        return self.points
    def rotateY3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateY3D(self.points[i],ang)
        return self.points
    def rotateZ3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateZ3D(self.points[i],ang)
        return self.points
    def projectionXZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionXZ3D(self.points[i])
        return self.points
    def projectionYX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionYX3D(self.points[i])
        return self.points
    def projectionZY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionZY3D(self.points[i])
        return self.points
    def shear3D(self,ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear3D(self.points[i],ang)
        return self.points
    def reflectX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX3D(self.points[i])
        return self.points
    def reflectY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY3D(self.points[i])
        return self.points
    def reflectZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectZ3D(self.points[i])
        return self.points
    def translate3D(self,x,y,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate3D(self.points[i],x,y,z)
        return self.points
    def scaleZ3D(self,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleZ3D(self.points[i],z)
        return self.points
    def scaleY3D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY3D(self.points[i],y)
        return self.points
    def scaleX3D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX3D(self.points[i],x)
        return self.points


class Parallelepiped:
    # Params:
        # x, y, z: Front-upper-left vertex coordinate
        # width height, length: Parallelepiped dimensions
    def __init__(self, x, y, z, width, height, length):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.length = length
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y, self.z])
        points_list.append([self.x, self.y - self.height, self.z])
        points_list.append(
            [self.x + self.length, self.y - self.height, self.z])
        points_list.append([self.x + self.length, self.y, self.z])
        points_list.append([self.x, self.y, self.z - self.width])
        points_list.append([self.x, self.y - self.height, self.z - self.width])
        points_list.append([self.x + self.length, self.y -
                            self.height, self.z - self.width])
        points_list.append([self.x + self.length, self.y, self.z - self.width])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        for i in range(1, 3):
            glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
            glVertex3f(self.points[i][0], self.points[i][1], self.points[i][2])
            glVertex3f(self.points[i + 1][0],
                       self.points[i + 1][1], self.points[i + 1][2])
        for i in range(3, 5):
            glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
            glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])
            glVertex3f(self.points[i][0], self.points[i][1], self.points[i][2])
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[1][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])

        glEnd()

    def rotateX3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateX3D(self.points[i],ang)
        return self.points
    def rotateY3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateY3D(self.points[i],ang)
        return self.points
    def rotateZ3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateZ3D(self.points[i],ang)
        return self.points
    def projectionXZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionXZ3D(self.points[i])
        return self.points
    def projectionYX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionYX3D(self.points[i])
        return self.points
    def projectionZY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionZY3D(self.points[i])
        return self.points
    def shear3D(self,ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear3D(self.points[i],ang)
        return self.points
    def reflectX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX3D(self.points[i])
        return self.points
    def reflectY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY3D(self.points[i])
        return self.points
    def reflectZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectZ3D(self.points[i])
        return self.points
    def translate3D(self,x,y,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate3D(self.points[i],x,y,z)
        return self.points
    def scaleZ3D(self,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleZ3D(self.points[i],z)
        return self.points
    def scaleY3D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY3D(self.points[i],y)
        return self.points
    def scaleX3D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX3D(self.points[i],x)
        return self.points


class Piramid:
    # Params:
        # x, y, z: Front-upper-left vertex coordinate
        # height: Distance to top vertex to base
        # width, length: Base's dimensions
    def __init__(self, x, y, z, height, width, length):
        self.x = x
        self.y = y
        self.z = z
        self.height = height
        self.width = width
        self.length = length
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y, self.z])
        points_list.append(
            [self.x - self.length / 2, self.y - self.height, self.z + self.width / 2])
        points_list.append(
            [self.x - self.length / 2, self.y - self.height, self.z - self.width / 2])
        points_list.append(
            [self.x + self.length / 2, self.y - self.height, self.z + self.width / 2])
        points_list.append(
            [self.x + self.length / 2, self.y - self.height, self.z - self.width / 2])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(0.0, 1.0, 0.0)
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])

        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glEnd()

    def rotateX3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateX3D(self.points[i],ang)
        return self.points
    def rotateY3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateY3D(self.points[i],ang)
        return self.points
    def rotateZ3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateZ3D(self.points[i],ang)
        return self.points
    def projectionXZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionXZ3D(self.points[i])
        return self.points
    def projectionYX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionYX3D(self.points[i])
        return self.points
    def projectionZY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionZY3D(self.points[i])
        return self.points
    def shear3D(self,ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear3D(self.points[i],ang)
        return self.points
    def reflectX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX3D(self.points[i])
        return self.points
    def reflectY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY3D(self.points[i])
        return self.points
    def reflectZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectZ3D(self.points[i])
        return self.points
    def translate3D(self,x,y,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate3D(self.points[i],x,y,z)
        return self.points
    def scaleZ3D(self,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleZ3D(self.points[i],z)
        return self.points
    def scaleY3D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY3D(self.points[i],y)
        return self.points
    def scaleX3D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX3D(self.points[i],x)
        return self.points


class Line3d:
    # Params:
        # origin: Beginning point coordinates passed as a array [x, y, z]
        # end: Final point coordinates passed as a array [x, y, z]
    def __init__(self, origin, end):
        self.origin = origin
        self.end = end
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.origin[0], self.origin[1], self.origin[2]])
        points_list.append([self.end[0], self.end[1], self.end[2]])
        return points_list

    def draw(self):
        glBegin(GL_LINES)
        glColor(1.0, 0.0, 0.0)
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])

        glEnd()

    def rotateX3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateX3D(self.points[i],ang)
        return self.points
    def rotateY3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateY3D(self.points[i],ang)
        return self.points
    def rotateZ3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateZ3D(self.points[i],ang)
        return self.points
    def projectionXZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionXZ3D(self.points[i])
        return self.points
    def projectionYX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionYX3D(self.points[i])
        return self.points
    def projectionZY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionZY3D(self.points[i])
        return self.points
    def shear3D(self,ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear3D(self.points[i],ang)
        return self.points
    def reflectX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX3D(self.points[i])
        return self.points
    def reflectY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY3D(self.points[i])
        return self.points
    def reflectZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectZ3D(self.points[i])
        return self.points
    def translate3D(self,x,y,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate3D(self.points[i],x,y,z)
        return self.points
    def scaleZ3D(self,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleZ3D(self.points[i],z)
        return self.points
    def scaleY3D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY3D(self.points[i],y)
        return self.points
    def scaleX3D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX3D(self.points[i],x)
        return self.points


class Sphere:
    # Params:
        # x, y, z: Center coordinates
        # radius
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
                    glColor(0.45, 0.9 - 0.04 * j, 0.45)
                    glVertex3f(
                        self.points[k1][0], self.points[k1][1], self.points[k1][2])
                    glVertex3f(
                        self.points[k2][0], self.points[k2][1], self.points[k2][2])
                    glVertex3f(
                        self.points[k1 + 1][0], self.points[k1 + 1][1], self.points[k1 + 1][2])

                if i != (self.stacks - 1):
                    glColor(0.2, 0.2,  0.9 - 0.04 * j)
                    glVertex3f(
                        self.points[k1 + 1][0], self.points[k1 + 1][1], self.points[k1 + 1][2])
                    glVertex3f(
                        self.points[k2][0], self.points[k2][1], self.points[k2][2])
                    glVertex3f(
                        self.points[k2 + 1][0], self.points[k2 + 1][1], self.points[k2 + 1][2])

                k1 = k1 + 1
                k2 = k2 + 1

            glEnd()

    def rotateX3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateX3D(self.points[i],ang)
        return self.points
    def rotateY3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateY3D(self.points[i],ang)
        return self.points
    def rotateZ3D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotateZ3D(self.points[i],ang)
        return self.points
    def projectionXZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionXZ3D(self.points[i])
        return self.points
    def projectionYX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionYX3D(self.points[i])
        return self.points
    def projectionZY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionZY3D(self.points[i])
        return self.points
    def shear3D(self,ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear3D(self.points[i],ang)
        return self.points
    def reflectX3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX3D(self.points[i])
        return self.points
    def reflectY3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY3D(self.points[i])
        return self.points
    def reflectZ3D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectZ3D(self.points[i])
        return self.points
    def translate3D(self,x,y,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate3D(self.points[i],x,y,z)
        return self.points
    def scaleZ3D(self,z):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleZ3D(self.points[i],z)
        return self.points
    def scaleY3D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY3D(self.points[i],y)
        return self.points
    def scaleX3D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX3D(self.points[i],x)
        return self.points
