from OpenGL.GL import *
from math import pi, sin, cos, tan
from transform import Transform


class Square:
    # Params:
        # x and y: Upper left vertex coordinates
        # width: Side size
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y])
        points_list.append([self.x + self.width, self.y])
        points_list.append([self.x + self.width, self.y - self.width])
        points_list.append([self.x, self.y - self.width])
        return points_list

    def draw(self):
        if(self.collinear()):
            glBegin(GL_LINES)
        else:
            glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[1][0], self.points[1][1])
        glVertex2f(self.points[2][0], self.points[2][1])

        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[2][0], self.points[2][1])
        glVertex2f(self.points[3][0], self.points[3][1])
        glEnd()

    def rotate2D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotate2D(self.points[i], ang)
        return self.points

    def projectionX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionX2D(self.points[i])
        return self.points

    def projectionY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionY2D(self.points[i])
        return self.points

    def shear(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear(self.points[i], ang)
        return self.points

    def reflectX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX2D(self.points[i])
        return self.points

    def reflectY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY2D(self.points[i])
        return self.points

    def translate2D(self, x, y):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate2D(self.points[i], x, y)
        return self.points

    def scaleY2D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY2D(self.points[i],y)
        return self.points
    def scaleX2D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX2D(self.points[i],x)
        return self.points

    def collinear(self): 
        """ Calculation the area of   
            triangle. We have skipped  
            multiplication with 0.5 to 
            avoid floating point computations """
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        for i in range(2, len(self.points)):
            a = x1 * (y2 - self.points[i][1]) + x2 * (self.points[i][1] - y1) + self.points[i][0] * (y1 - y2)
            if (a != 0): 
                return False
        return True


class Rectangle:
    # Params:
        # x and y: Upper left vertex coordinates
        # width and height: rectangles dimensions
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y])
        points_list.append([self.x + self.width, self.y])
        points_list.append([self.x + self.width, self.y - self.height])
        points_list.append([self.x, self.y - self.height])
        return points_list

    def draw(self):
        if (self.collinear()):
            glBegin(GL_LINES)
        else:
            glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[1][0], self.points[1][1])
        glVertex2f(self.points[2][0], self.points[2][1])

        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[2][0], self.points[2][1])
        glVertex2f(self.points[3][0], self.points[3][1])
        glEnd()

    def rotate2D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotate2D(self.points[i], ang)
        return self.points

    def projectionX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionX2D(self.points[i])
        return self.points

    def projectionY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionY2D(self.points[i])
        return self.points

    def shear(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear(self.points[i], ang)
        return self.points

    def reflectX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX2D(self.points[i])
        return self.points

    def reflectY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY2D(self.points[i])
        return self.points

    def translate2D(self, x, y):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate2D(self.points[i], x, y)
        return self.points

    def scaleY2D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY2D(self.points[i],y)
        return self.points
    def scaleX2D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX2D(self.points[i],x)
        return self.points

    def collinear(self): 
        """ Calculation the area of   
            triangle. We have skipped  
            multiplication with 0.5 to 
            avoid floating point computations """
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        for i in range(2, len(self.points)):
            a = x1 * (y2 - self.points[i][1]) + x2 * (self.points[i][1] - y1) + self.points[i][0] * (y1 - y2)
            if (a != 0): 
                return False
        return True


class Triangle:
    # Params:
        # A, B, C: Each vertex coordinates passed as a array [x, y]
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.A[0], self.A[1]])
        points_list.append([self.B[0], self.B[1]])
        points_list.append([self.C[0], self.C[1]])
        return points_list

    def draw(self):
        if(self.collinear()):
            glBegin(GL_LINES)
        else:
            glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[1][0], self.points[1][1])
        glVertex2f(self.points[2][0], self.points[2][1])

        glEnd()

    def rotate2D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotate2D(self.points[i], ang)
        return self.points

    def projectionX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionX2D(self.points[i])
        return self.points

    def projectionY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionY2D(self.points[i])
        return self.points

    def shear(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear(self.points[i], ang)
        return self.points

    def reflectX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX2D(self.points[i])
        return self.points

    def reflectY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY2D(self.points[i])
        return self.points

    def translate2D(self, x, y):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate2D(self.points[i], x, y)
        return self.points

    def scaleY2D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY2D(self.points[i],y)
        return self.points
    def scaleX2D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX2D(self.points[i],x)
        return self.points

    def collinear(self): 
        """ Calculation the area of   
            triangle. We have skipped  
            multiplication with 0.5 to 
            avoid floating point computations """
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        for i in range(2, len(self.points)):
            a = x1 * (y2 - self.points[i][1]) + x2 * (self.points[i][1] - y1) + self.points[i][0] * (y1 - y2)
            if (a != 0): 
                return False
        return True


class Line:
    # Params:
        # origin: Beginning point coordinates passed as a array [x, y]
        # end: Final point coordinates passed as a array [x, y]
    def __init__(self, origin, end):
        self.origin = origin
        self.end = end
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.origin[0], self.origin[1]])
        points_list.append([self.end[0], self.end[1]])
        return points_list

    def draw(self):
        if(self.points[0] == self.points[1]):
            glPointSize(4.0)
            glBegin(GL_POINTS)
            # glLineWidth(10)
        else:
            glBegin(GL_LINES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[1][0], self.points[1][1])

        glEnd()

    def rotate2D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotate2D(self.points[i], ang)
        return self.points

    def projectionX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionX2D(self.points[i])
        return self.points

    def projectionY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionY2D(self.points[i])
        return self.points

    def shear(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear(self.points[i], ang)
        return self.points

    def reflectX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX2D(self.points[i])
        return self.points

    def reflectY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY2D(self.points[i])
        return self.points

    def translate2D(self, x, y):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate2D(self.points[i], x, y)
        return self.points

    def scaleY2D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY2D(self.points[i],y)
        return self.points
    def scaleX2D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX2D(self.points[i],x)
        return self.points


class Circle:
    # Params:
        # x, y: Center coordinates
        # radius: Radius lenght
        # sectors: Number of triangles that will compose the circle
    def __init__(self, x, y, radius, sectors):
        self.x = x
        self.y = y
        self.radius = radius
        self.sectors = sectors
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        ang = pi * 2 / self.sectors
        for i in range(0, self.sectors):
            points_list.append(
                [self.x + (self.radius * cos(i * ang)), self.y + (self.radius * sin(i * ang))])
        return points_list

    def draw(self):
        if(self.collinear()):
            glBegin(GL_LINES)
        else:
            glBegin(GL_TRIANGLES)

        for i in range(0, self.sectors):
            if(i == (self.sectors - 1)):
                glVertex2f(self.x, self.y)
                glVertex2f(self.points[i][0], self.points[i][1])
                glVertex2f(self.points[0][0], self.points[0][1])
            else:
                glVertex2f(self.x, self.y)
                glVertex2f(self.points[i][0], self.points[i][1])
                glVertex2f(self.points[i + 1][0], self.points[i + 1][1])
        glEnd()

    def rotate2D(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().rotate2D(self.points[i], ang)
        return self.points

    def projectionX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionX2D(self.points[i])
        return self.points

    def projectionY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().projectionY2D(self.points[i])
        return self.points

    def shear(self, ang):
        for i in range(len(self.points)):
            self.points[i] = Transform().shear(self.points[i], ang)
        return self.points

    def reflectX2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectX2D(self.points[i])
        return self.points

    def reflectY2D(self):
        for i in range(len(self.points)):
            self.points[i] = Transform().reflectY2D(self.points[i])
        return self.points

    def translate2D(self, x, y):
        for i in range(len(self.points)):
            self.points[i] = Transform().translate2D(self.points[i], x, y)
        return self.points

    def scaleY2D(self,y):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleY2D(self.points[i],y)
        return self.points
    def scaleX2D(self,x):
        for i in range(len(self.points)):
            self.points[i] = Transform().scaleX2D(self.points[i],x)
        return self.points

    def collinear(self): 
        """ Calculation the area of   
            triangle. We have skipped  
            multiplication with 0.5 to 
            avoid floating point computations """
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        for i in range(2, len(self.points)):
            a = x1 * (y2 - self.points[i][1]) + x2 * (self.points[i][1] - y1) + self.points[i][0] * (y1 - y2)
            if (a != 0): 
                return False
        return True
