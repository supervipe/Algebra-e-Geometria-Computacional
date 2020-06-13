from math import pi,sin,cos,tan,sqrt
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
                    res += ('{:>5.5f}    '.format(self[i, j]))
                else: 
                    res += (' {:>5.5f}    '.format(self[i, j]))
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

    def eigen(self):
        A = Matrix(self.rows, self.cols, self.data.copy())
        eigenvalues = Matrix(self.rows, 1)
        eigenvectors = Matrix(self.rows, self.cols + 1)
        Ax0 = Matrix(self.rows, 1)
        vetores = Matrix(self.rows, self.cols + 1)
        x0 = Matrix(self.rows, 1)
        x0[1,1] = 1
        
        for j in range(1, A.rows + 1):
            B = A
            pre = 1
            lyx = Matrix(2,1)
            while(pre > 0.0000000001):
                lyx[1,1] = lyx[2,1]
                Ax0 = A.dot(x0)
                soma = 0
                for i in range(1, A.rows + 1):
                    soma += (Ax0[i,1] * Ax0[i,1])
                soma = 1/sqrt(soma)
                x0 = soma*(Ax0)
                Ax0 = Ax0.transpose()
                Ax0 = Ax0.dot(x0)
                lyx[2,1] = Ax0[1,1]
                pre = (lyx[2,1] - lyx[1,1]) / lyx[2,1]

            eigenvalues[j,1] = lyx[2,1]
            eigenvectors[j,1] = lyx[2,1]
            for k in range(1, eigenvectors.cols):
                eigenvectors[j, k +1] = x0[k,1] 

            A = B
            Ax0 = Matrix(self.rows, self.cols)
            for b1 in range(1, A.rows + 1):
                for b2 in range(1, A.rows + 1):
                    Ax0[b1,b2] = eigenvectors[j,b1 + 1] * eigenvectors[j, b2 + 1] * lyx[2,1] 
            A = A - (Ax0)

        return eigenvalues, eigenvectors

    def pagerank(self):
        A = Matrix(self.rows, self.cols, self.data.copy())
        At = A
        a0 = Matrix(self.rows, 1)
        multA = 1
        somaa0 = 0
        soma = 0
        cont = 1
        valor = 5
        sub = 1

        for i in range(1, A.rows + 1):
            for j in range(1, A.cols + 1):
                somaa0 += A[j,i]
            a0[i,1] = somaa0
            somaa0 = 0
        
        while(sub> 0.0000005):
            if(soma == 0):
                for a2 in range(1, A.rows + 1):
                    soma += (a0[a2,1] * a0[a2,1])
                soma = 1/sqrt(soma)
                a0 = a0 * soma
            else:
                while(multA[cont, 1] == 0):
                    cont +=1
                valor = multA[cont, 1]
            At = A.transpose()
            multA = At.dot(A)
            multA = multA.dot(a0)
            somaF = 0
            for a3 in range(1, A.rows + 1):
                somaF += (multA[a3,1] * multA[a3,1])
            somaF = 1/sqrt(somaF)
            multA = multA * somaF
            a0 = multA
            sub = abs(valor - multA[cont,1])

        return a0




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
