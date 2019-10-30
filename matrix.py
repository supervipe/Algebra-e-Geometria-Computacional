from math import pi,sin,cos,tan
class Matrix:

    def __init__(self, rows, cols, data = []):
        self.rows = rows
        self.cols = cols
        self._init_data(data)

    def __getitem__(self, key):
        i, j = key    
        if(i > self.rows or j > self.cols):
            print("Invalido!")
        else:    
            return self.data[(j-1) + (i-1) * self.cols]

    def __setitem__(self, key, value):
        i, j = key
        if(i > self.rows or j > self.cols):
            print("Invalido!")
        else:
            self.data[(j-1) + (i-1) * self.cols] = value

    def __add__(self, other):
        res = Matrix(self.rows, self.cols)
        
        if type(other) == int or type(other) == float:
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] + other

            return res
        elif type(other) == Matrix:
            if self.sameSize(self, other):
                for i in range(1,self.rows + 1):
                    for j in range(1,self.cols + 1):
                        res[i, j] = self[i, j] + other[i, j]

                return res
            else:
                print("Matrizes de tamanhos diferentes!") 
        else:
            print("Incapaz de somar!")   

    def __sub__(self, other):
        res = Matrix(self.rows, self.cols)
        
        if type(other) == int or type(other) == float:
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] - other

            return res
        elif type(other) == Matrix:
            if self.sameSize(self, other):
                for i in range(1,self.rows + 1):
                    for j in range(1,self.cols + 1):
                        res[i, j] = self[i, j] - other[i, j]

                return res
            else:
                print("Matrizes de tamanhos diferentes!") 
        else:
            print("Incapaz de subtrair!")
        


    def __mul__(self, other):
        res = Matrix(self.rows, self.cols)
        
        if type(other) == int or type(other) == float:
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] * other

            return res
        elif type(other) == Matrix:
            if self.sameSize(self, other):
                for i in range(1,self.rows + 1):
                    for j in range(1,self.cols + 1):
                        res[i, j] = self[i, j] * other[i, j]

                return res
            else:
                print("Matrizes de tamanhos diferentes!") 
        else:
            print("Incapaz de multiplicar!")
        

    def __truediv__(self, other):
        res = Matrix(self.rows, self.cols)
        
        if type(other) == int or type(other) == float:
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    if (other == 0.0):
                        print("Divisao por zero nao possivel!")
                        break
                    else:    
                        res[i, j] = self[i, j] / other
                        
            return res
        elif type(other) == Matrix:
            if self.sameSize(self, other):
                for i in range(1,self.rows + 1):
                    for j in range(1,self.cols + 1):
                        if (other[i, j] == 0):
                            print("Divisao por zero nao possivel!")
                            break
                        else:    
                            res[i, j] = (self[i, j]) / (other[i, j])
                return res
            else:
                print("Matrizes de tamanhos diferentes!")
        else:
            print("Incapaz de dividir!")

    def dot(self, other): 
        res = Matrix(self.rows, other.cols) 

        for i in range(1,self.rows + 1): 
            for j in range(1, other.cols + 1): 
                for k in range(1, self.cols + 1): 
                    res[i, j] = self[i, k] * other [k, j] + res[i,j] 
        
        return res 

    def __radd__(self, other):
        return self.__add__(other)
        
    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)  

    def sameSize(self,a,b):
        return True if a.rows == b.rows and a.cols == b.cols else False   

    def __repr__(self): 
        res = " "
        for i in range (1, self.rows + 1): 
            for j in range (1, self.cols + 1): 
                if self [i, j] < 0: 
                    res += ('{:>4.4f}    '.format(self[i, j]))
                else: 
                    res += (' {:>4.4f}    '.format(self[i, j]))
            res += ('\n')
        return res

    def gauss_jordan(self):
        res = Matrix(self.rows, self.cols, self.data.copy())
        newma = res
        for i in range(1, newma.rows):
            maximoElemento = abs(newma[i, i])
            maximaLinha = i 
            for k in range(i +1,newma.rows+1):
                if abs(newma[k, i]) > maximoElemento:
                    maximoElemento = abs(newma[k, i])
                    maximaLinha = k
            for k in range(i, newma.cols+1): 
                newma[maximaLinha, k],newma[i, k] = newma[i, k],newma[maximaLinha, k] 
            for k in range(i + 1, newma.rows+1):
                d = -newma[k, i]/newma[i, i] 
                for j in range (i , newma.cols +1):
                    if (i == j):
                        newma[k, j] = 0
                    else:
                        newma[k, j] += d * newma[i, j]

        for w in range(newma.rows, 1,-1):
            for k in range(w - 1, 0,-1):
                    y = -newma[k, w]/newma[w, w] 
                    for j in range (newma.cols, w -1, -1):
                        if (w == j):
                            newma[k, j] = 0
                        else:
                            newma[k, j] += y * newma[w, j]

        for i in range(newma.rows, 0, -1):
            newma[i, newma.rows+1] = newma[i, newma.rows+1]/newma[i,i]
            newma[i,i] = 1
        
        return newma

    def inverse(self):
        matrix1 = Matrix(self.rows, self.cols, self.data.copy())
        newma = Matrix(self.rows,self.cols*2)
        for p1 in range(1,newma.rows+1):
            for j in range(1, newma.rows + 1):
                newma[p1,j] = matrix1[p1,j]
        for p2 in range(1,newma.rows+1):
            for i in range(newma.rows + 1, newma.cols +1):
                if( p2 ==(i - newma.rows)):
                    newma[p2,i] = 1
                else:
                    newma[p2,i] = 0
        for i in range(1, newma.rows):
            maximoElemento = abs(newma[i, i])
            maximaLinha = i 
            for k in range(i +1,newma.rows+1):
                if abs(newma[k, i]) > maximoElemento:
                    maximoElemento = abs(newma[k, i])
                    maximaLinha = k
            for k in range(i, newma.cols+1): 
                newma[maximaLinha, k],newma[i, k] = newma[i, k],newma[maximaLinha, k] 
            for k in range(i + 1, newma.rows+1):
                d = -newma[k, i]/newma[i, i] 
                for j in range (i , newma.cols +1):
                    if (i == j):
                        newma[k, j] = 0
                    else:
                        newma[k, j] += d * newma[i, j]

        for w in range(newma.rows, 1,-1):
            for k in range(w - 1, 0,-1):
                    y = -newma[k, w]/newma[w, w] 
                    for j in range (newma.cols, w -1, -1):
                        if (w == j):
                            newma[k, j] = 0
                        else:
                            newma[k, j] += y * newma[w, j]

        for i in range(newma.rows, 0, -1):
            for j in range(newma.rows + 1, newma.cols + 1):
                newma[i, j] = newma[i,j]/newma[i,i]
            newma[i,i] = 1
        
        return newma

    def transpose(self):
        res = Matrix(self.rows, self.cols, self.data.copy())
        newma = Matrix(self.cols, self.rows)
        for i in range(1, res.rows+1):
            for j in range(1, res.cols+1):
                newma[j,i] = res[i,j]
        return newma

    def LU(self):
        u = Matrix(self.rows, self.cols, self.data.copy())
        l = Matrix(self.rows, self.cols)

        for x in range(1, self.rows+1):
            l[x, x] = 1
        for i in range(1, u.rows+1):
            for k in range(i + 1, u.rows+1):
                d = -u[k, i]/u[i, i] 
                l[k,i] = -d
                for j in range (i , u.cols +1):
                    if (i == j):
                        u[k, j] = 0
                    else:
                        u[k, j] += d * u[i, j]
        return l,u

    def LDU(self):
        u = Matrix(self.rows, self.cols, self.data.copy())
        l = Matrix(self.rows, self.cols)
        d = Matrix(self.rows, self.cols)

        for i in range(1, u.rows+1):
            l[i,i] = 1
            for k in range(i + 1, u.rows+1):
                c = -u[k, i]/u[i, i] 
                l[k,i] = -c
                for j in range (i , u.cols +1):
                    if (i == j):
                        u[k, j] = 0
                    else:
                        u[k, j] += c * u[i, j]
        for i in range(1, u.rows +1):
            d[i, i] = u[i,i]
            for j in range(1, u.cols +1):
                u[i,j] /= d[i,i]

        return l,d,u

    def __str__(self):
        return __repr__(self)
        
    def _init_data(self, data):
        if data:
            try:
                if len(data) == self.rows * self.cols:
                    self.data = data
                else:
                    raise Exception('Init error', 'The data is incompatible with matrix size')
            except Exception as e:
                self._print_error(e)
        else:
            self.data = [0] * (self.rows * self.cols)
