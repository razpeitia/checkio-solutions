points = [(0, 0), (0, 9), (9, 0)]
step = 0

class Matrix(object):
    def __init__(self, n):
        self.size = n
        self.matrix = [
            [0] * n for i in range(n)
        ]
        self.__max = None

    def circle(self, i_, j_, r):
        for i in range(10):
            for j in range(10):
                d = ((i - i_) ** 2) + ((j - j_) ** 2)
                d = round(d ** .5)
                if d == r:
                    self.matrix[i][j] += 1

    @property
    def max(self):
        if self.__max is None:
            self.__max = max(sum(self.matrix, []))
        return self.__max

    def is_max_unique(self):
        c = 0
        for i in range(10):
            for j in range(10):
                if self.matrix[i][j] == self.max:
                    c += 1
        return c == 1

    def get_max_pos(self):
        for i in range(10):
            for j in range(10):
                if self.matrix[i][j] == self.max:
                    return (i, j)


    def __str__(self):
        return '\n'.join(' '.join('%2d' % self.matrix[i][j] for j in range(10)) for i in range(10))

    def __repr__(self):
        return self.__str__()

def checkio(probes):
    global step, points
    if not probes:
        step = 0
    else:
        step += 1
    
    if step == 3:
        # Resuelve aqui
        # Tienes 3, circulos
        # Solo tienes que calcular donde se intersectan
        matrix = Matrix(10)
        for i, j, r in probes:
            matrix.circle(i, j, r)
        if matrix.is_max_unique():
            # print matrix
            # print matrix.max
            ans = matrix.get_max_pos()
            # print ans
            return ans
    else:
        return points[step]
