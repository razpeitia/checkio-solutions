class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.h = len(matrix)
        self.w = len(matrix[0])

    def submatrix(self, point1, point2):
        y1, x1 = point1
        y2, x2 = point2
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1

        matrix = [[self.matrix[y][x] for x in range(x1, x2)] for y in range(y1, y2)]
        return Matrix(matrix)

    def compare(self, block):
        diff = 0
        for i in range(self.h):
            for j in range(self.w):
                if str(self.matrix[i][j]) != str(block[i][j]):
                    diff += 1
        return diff

    def get_digit(self):
        global DIGITS
        for i, digit in enumerate(DIGITS):
            if self.compare(digit) <= 1:
                return (i + 1) % 10

    def __getitem__(self, key):
        return self.matrix[key]

    def __str__(self):
        d = {'0': '-', '1': 'X', 0: '-', 1: 'X'}
        return '\n'.join(''.join(d[c] for c in row) for row in self.matrix)

FONT = Matrix(["00100111011101010111001101110111001101100",
            "01100001000101010100010000010101010101010",
            "00100011001001110110011100100111011101010",
            "00100100000100010001010101000101000101010",
            "00100111011100010110001101000111011000110",])
h, w = FONT.h, FONT.w
numbers = (w - 1) // 4

DIGITS = [
    FONT.submatrix( (0, i*4), (5, (i+1)*4) )
for i in range(numbers)]

def checkio(image):
    h, w = len(image), len(image[0])
    numbers = (w - 1) // 4
    
    blocks = [
        (
            (0, i*4),
            (5, (i+1)*4),
        )
        for i in range(numbers)]
    matrix = Matrix(image)
    digits = ''.join(str(matrix.submatrix(*block).get_digit()) for block in blocks)
    return int(digits)
    
    
    
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"

