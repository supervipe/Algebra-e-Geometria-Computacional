class Matrix:
    def __init__(self, rows, cols, data=[]):
        try:
            if (type(rows) != int or type(cols) != int):
                raise Exception(
                    'Data Type', 'The provided row or column is not a integer.')
            if (rows < 0 or cols < 0):
                raise Exception(
                    'Invalid Value', 'The provided number row and column must be greater than zero.')
            self.rows = rows
            self.cols = cols
            self._init_data(data)
        except Exception as e:
            self._print_error(e)

    def __getitem__(self, key):
        try:
            i, j = key
            if not self._row_limit(i):
                raise Exception(
                    'Row index', 'The provided row index {} is out of range.'.format(i))
            if not self._col_limit(j):
                raise Exception(
                    'Col index', 'The provided col index {} is out of range.'.format(j))
            return self.data[(j - 1) + (i - 1) * self.cols]
        except Exception as e:
            self._print_error(e)

    def __setitem__(self, key, value):
        try:
            i, j = key
            if not self._row_limit(i):
                raise Exception(
                    'Row index', 'The provided row index {} is out of range.'.format(i))
            if not self._col_limit(j):
                raise Exception(
                    'Col index', 'The provided col index {} is out of range.'.format(j))
            self.data[(j - 1) + (i - 1) * self.cols] = value
        except Exception as e:
            self._print_error(e)

    def __repr__(self):
        print('')
        for i in range(1, self.rows+1):
            for j in range(1, self.cols+1):
                print("{0:.4f}".format(self[i, j]), end="   ")
            print('')
        return ''

    def __str__(self) -> str:
        print('')
        for i in range(1, self.rows+1):
            for j in range(1, self.cols+1):
                print("{0:.4f}".format(self[i, j]), end="   ")
            print('')
        return ''

    def __radd__(self, other):
        return self.__add__(other)

    def __add__(self, other):
        try:
            if self.isNumber(other):
                res = Matrix(self.rows, self.cols)
                for i in range(1, self.rows + 1):
                    for j in range(1, self.cols + 1):
                        res[i, j] = self[i, j] + other
                return res
            elif self.isMatrix(other):
                if self._same_size(self, other):
                    res = Matrix(self.rows, self.cols)
                    for i in range(1, self.rows + 1):
                        for j in range(1, self.cols + 1):
                            res[i, j] = self[i, j] + other[i, j]
                    return res
                else:
                    raise Exception(
                        'Matrix size', 'The matrixes are incompatibles.')
        except Exception as e:
            self._print_error(e)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __sub__(self, other):
        try:
            if self.isNumber(other):
                res = Matrix(self.rows, self.cols)
                for i in range(1, self.rows + 1):
                    for j in range(1, self.cols + 1):
                        res[i, j] = self[i, j] - other
                return res
            elif self.isMatrix(other):
                if self._same_size(self, other):
                    res = Matrix(self.rows, self.cols)
                    for i in range(1, self.rows + 1):
                        for j in range(1, self.cols + 1):
                            res[i, j] = self[i, j] - other[i, j]
                    return res
                else:
                    raise Exception(
                        'Matrix size', 'The matrixes are incompatibles.')
        except Exception as e:
            self._print_error(e)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        try:
            if self.isNumber(other):
                res = Matrix(self.rows, self.cols)
                for i in range(1, self.rows + 1):
                    for j in range(1, self.cols + 1):
                        res[i, j] = self[i, j] * other
                return res
            elif self.isMatrix(other):
                if self._same_size(self, other):
                    res = Matrix(self.rows, self.cols)
                    for i in range(1, self.rows + 1):
                        for j in range(1, self.cols + 1):
                            res[i, j] = self[i, j] * other[i, j]
                    return res
                else:
                    raise Exception(
                        'Matrix size', 'The matrixes are incompatibles.')
        except Exception as e:
            self._print_error(e)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __truediv__(self, other):
        try:
            if self.isNumber(other):
                if other == 0:
                    raise Exception('Invalid Operation', 'Division by Zero.')
                res = Matrix(self.rows, self.cols)
                for i in range(1, self.rows + 1):
                    for j in range(1, self.cols + 1):
                        res[i, j] = self[i, j] / other
                return res
            elif self.isMatrix(other):
                if self._same_size(self, other):
                    res = Matrix(self.rows, self.cols)
                    for i in range(1, self.rows + 1):
                        for j in range(1, self.cols + 1):
                            if other[i, j] == 0:
                                raise Exception(
                                    'Invalid Operation', 'Division by Zero.')
                            res[i, j] = self[i, j] / other[i, j]
                    return res
                else:
                    raise Exception(
                        'Matrix size', 'The matrixes are incompatibles.')
        except Exception as e:
            self._print_error(e)

    def dot(self, other):
        try:
            if self.isMatrix(other):
                if self._matrix_dot_compatibility(self, other):
                    res = Matrix(self.rows, other.cols)
                    for i in range(1, self.rows + 1):
                        for j in range(1, other.cols + 1):
                            for k in range(1, self.cols + 1):
                                res[i, j] += self[i, k] * other[k, j]
                    return res
                else:
                    raise Exception('Matrix size', 'The left matrix is {}x{} and right matrix is {}x{}.'.format(
                        self.rows, self.cols, other.rows, other.cols))
            else:
                raise Exception('Data type', 'The parameter must be a Matrix.')
        except Exception as e:
            self._print_error(e)

    def transpose(self):
        res = Matrix(self.cols, self.rows)
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                res[j, i] = self[i, j]
        return res

    def gauss_jordan(self):
        if self.cols > self.rows:
            res = self

            for j in range(1, self.rows + 1):  # Colunas menos a ultima (1 a 3)
                for i in range(1, self.rows + 1):  # Linhas até a diagonal principal (3 a 1)
                    # Diagonal principal
                    if(i == j):
                        if(res[i, j] != 1):
                            # Numero valor do numero da posição
                            div = res[i, j]
                            # Colunas para a conta
                            for s in range(j, self.cols + 1):
                                res[i, s] /= div
                    # Abaixo da Diagonal principal
                    elif(i > j):
                        if(res[i, j] != 0):
                            # CALCULO PRA DEIXAR IGUAL A 0
                            if(j == 1):
                                x = 1  # variável para a linha que será utilizada para somar com a linha 'i'
                            else:
                                x = i - 1
                            # multiplicador para linha que irá somar e zerar o elemento [i,j]
                            mult = (res[i, j] * (-1)) / res[x, j]
                            # 's' colunas para somar cada elemento da linha
                            for s in range(1, self.cols + 1):
                                res[i, s] += res[x, s] * mult

            for j in range(self.rows, 1, -1):  # Da penultima coluna até a segunda
                for i in range(self.rows - 1, 0, -1):  # Linhas acima da diagonal principal
                    # Acima da diagonal principal
                    if(j > i):
                        if(res[i, j] != 0):
                            x = j
                            # multiplicador para linha que irá somar e zerar o elemento [i,j]
                            mult = (res[i, j] * (-1)) / res[x, j]
                            # 's' colunas para somar cada elemento da linha
                            for s in range(1, self.cols + 1):
                                res[i, s] += res[x, s] * mult
        return res

    def inverse(self):
        try:
            if self.isSquare():
                # Criando matriz com o dobro de colunas para a matriz identidade ficar junta
                res = Matrix(self.rows, 2 * self.cols)
                # Setando os valores da matriz originais com a identidade
                for i in range(1, res.rows + 1):
                    for j in range(1, res.cols + 1):
                        if(j <= self.cols):  # Matriz Original (self)
                            res[i, j] = self[i, j]
                        elif(i == j - self.cols):  # Diagonal da matriz identidade (1's)
                            res[i, j] = 1
                        else:  # Resto da matriz identidade (0's)
                            res[i, j] = 0
                res = res.gauss_jordan()

                resreal = Matrix(self.rows, self.cols)
                for i in range(1, self.rows + 1):
                    for j in range(1, self.cols + 1):
                        resreal[i, j] = res[i, j + self.cols]
                return resreal
            else:
                raise Exception(
                    'Matrix size', 'The matrix must be square to have a inverse.')
        except Exception as e:
            self._print_error(e)

    def solve(self):
        try:
            if self.cols == self.rows + 1:
                res = self.gauss_jordan()
                resreal = Matrix(self.rows, 1)
                for i in range(1, self.rows + 1):
                    resreal[i, 1] = res[i, self.cols]
                return resreal
            else:
                raise Exception(
                    'Matrix size', 'The matrix is not compatible.')
        except Exception as e:
            self._print_error(e)

    def _init_data(self, data):
        if data:
            try:
                if len(data) == self.rows * self.cols:
                    self.data = data
                else:
                    raise Exception(
                        'Init error', 'The data is incompatible with matrix size')
            except Exception as e:
                self._print_error(e)
        else:
            self.data = [0] * (self.rows * self.cols)

    def isNumber(self, a):
        return True if (type(a) == int or type(a) == float) else False

    def isMatrix(self, a):
        return True if type(a) == Matrix else False

    def isSquare(self):
        return True if self.rows == self.cols else False

    def _matrix_dot_compatibility(self, a, b):
        return True if a.cols == b.rows else False

    def _same_size(self, a, b):
        return True if a.rows == b.rows and a.cols == b.cols else False

    def _row_limit(self, i):
        return True if i >= 1 and i <= self.rows else False

    def _col_limit(self, j):
        return True if j >= 1 and j <= self.cols else False

    def _print_error(self, e):
        kind, error = e.args
        print('ERROR[{}]: {}'.format(kind, error))