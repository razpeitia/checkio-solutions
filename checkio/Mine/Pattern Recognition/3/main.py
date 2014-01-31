class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.w, self.h = len(matrix[0]), len(matrix)

    def match(self, pos, pattern):
        h, w = pattern.h, pattern.w
        di, dj = pos
        for i in range(h):
            for j in range(w):
                if pattern[i][j] != self.matrix[di+i][dj+j]:
                    return False
        return True

    def mark(self, pos, w, h):
        lookup = {1: 3, 0: 2}
        di, dj = pos
        for i in range(di, di+h):
            for j in range(dj, dj+w):
                self.matrix[i][j] = lookup[self.matrix[i][j]]

    def scan(self, pattern):
        i = 0
        while i <= (self.h - pattern.h):
            j = 0
            row_flag = False
            while j <= (self.w - pattern.w):
                pos = i, j
                if self.match(pos, pattern):
                    self.mark(pos, pattern.w, pattern.h)
                    j += pattern.w
                else:
                    j += 1
            i += 1

    def __getitem__(self, key):
        return self.matrix[key]

    def __str__(self):
        return '\n'.join(' '.join(str(c) for c in r) for r in self.matrix) + '\n'


def checkio(pattern, image):
    pattern = Matrix(pattern)
    image = Matrix(image)
    image.scan(pattern)

    return image.matrix

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 0], [1, 1]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                          [0, 3, 3, 0, 0],
                                          [3, 2, 1, 3, 2],
                                          [3, 3, 0, 3, 3],
                                          [0, 1, 1, 0, 0]], "First"
    assert checkio([[1, 1], [1, 1]],
                   [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]) == [[3, 3, 1],
                                    [3, 3, 1],
                                    [1, 1, 1]], "Second"
    assert checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                         [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                         [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                         [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                         [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                         [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "Third"

