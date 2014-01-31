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


def checkio(data):
    matrix = Matrix(data)
    return matrix.determinant()

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[4, 3], [6, 3]]) == -6, 'First example'

    assert checkio([[1, 3, 2],
                    [1, 1, 4],
                    [2, 2, 1]]) == 14, 'Second example'

