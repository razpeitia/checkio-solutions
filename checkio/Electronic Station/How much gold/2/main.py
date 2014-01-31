from fractions import Fraction

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def replace_col(self, col, data):
        for i in range(self.n):
            self.matrix[i][col] = data[i]
    
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
        return '\n'.join(str(row) for row in self.matrix)

METALS = ('gold', 'tin', 'iron', 'copper')


def checkio(alloys):
    """
        Find proportion of gold
    """
    A = []
    b = []
    for k, v in alloys.items():
        metals = k.split('-')
        eq = []
        for metal in METALS:
            if metal in metals:
                eq.append(Fraction(1, 1))
            else:
                eq.append(Fraction(0, 1))
        A.append(eq)
        b.append(v)
    A.append([Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1)])
    b.append(Fraction(1, 1))

    A = Matrix(A)
    D = A.determinant()
    A.replace_col(0, b)
    Dx = A.determinant()

    return Dx / D

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({
        'gold-tin': Fraction(1, 2),
        'gold-iron': Fraction(1, 3),
        'gold-copper': Fraction(1, 4),
        }) == Fraction(1, 24), "1/24 of gold"
    assert checkio({
        'tin-iron': Fraction(1, 2),
        'iron-copper': Fraction(1, 2),
        'copper-tin': Fraction(1, 2),
        }) == Fraction(1, 4), "quarter"

