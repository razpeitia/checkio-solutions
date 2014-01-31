class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
    
    def sub_determinant(self, i, j):
        matrix = []
        for i_ in range(self.n):
            row = []
            for j_ in range(self.n):
                if not (i_ == i or j_ == j):
                    row.append(self.matrix[i_][j_])
            if row:
                matrix.append(row)
        return Matrix(matrix)
    
    def determinant(self):
        if self.n == 1:
            return self.matrix[0][0]
        elif self.n == 2:
            (a, b), (c, d) = self.matrix
            return a*d - b*c
        else:
            return sum(
                ((-1) ** i) * self.matrix[0][i] * self.sub_determinant(0, i).determinant()
                for i in range(self.n)
            )
    def __str__(self):
        return "\n".join(' '.join(str(cell) for cell in row) for row in self.matrix)

class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def mid(self, point):
        return Point((self.x + point.x) / 2.0, (self.y + point.y) / 2.0)

    def grad(self, point):
        return (self.y - point.y) / float(self.x - point.x)

    def igrad(self, point):
        return -(float(self.x - point.x) / (self.y - point.y))

    def distance(self, point):
        x = ((self.x - point.x) ** 2)
        y = ((self.y - point.y) ** 2)
        return (x + y) ** .5

    def __str__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)


class Line(object):
    def __init__(self, p, m):
        self.p = p
        self.m = m

    def intersection(self, line):
        a, b, e = -self.m, 1.0, self.p.y - (self.m * self.p.x)
        c, d, f = -line.m, 1.0, line.p.y - (line.m * line.p.x)
        
        # Cramer's rule
        D = Matrix([
                [a, b], 
                [c, d]
            ]
        )
        Dx = Matrix([
                [e, b],
                [f, d]
            ]
        )
        Dy = Matrix([
                [a, e],
                [c, f]
            ]
        )
        
        D = D.determinant()
        Dx = Dx.determinant()
        Dy = Dy.determinant()

        x = Dx / D
        y = Dy / D

        return Point(x, y)

    def __str__(self):
        return "(%s, %.2f)" % (self.p, self.m)

def fmt(num):
    num = "%.2f" % num
    while num.endswith('0'):
        num = num[:-1]
    if num.endswith('.'):
        num = num[:-1]
    return num

def checkio(data):
    a, b, c = eval(data)
    a, b, c = Point(*a), Point(*b), Point(*c)
    options = [(a, b), (b, c), (c, a)]
    lines = []
    for A, B in options:
        try:
            line = Line(A.mid(B), A.igrad(B))
            lines.append(line)
        except ZeroDivisionError:
            pass
    l1, l2 = lines[0], lines[1]
    center = l1.intersection(l2)
    radius = center.distance(a)
    x = fmt(-center.x)
    y = fmt(-center.y)
    radius = fmt(radius)
    ans = "(x%s)^2+(y%s)^2=%s^2" % (x, y, radius)
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert checkio("(7,7),(4,3),(1,8)") == "(x-3.8)^2+(y-6.28)^2=3.28^2"
