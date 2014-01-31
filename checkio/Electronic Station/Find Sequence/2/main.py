def checkio(matr):
    '''
    Given the matrix NxN (4<=N<=10). Check if 4 numbers in sequence in a column or in a row or diagonally exist.
    '''
    def check(arr):
        return len(set(arr)) == 1

    def check2(arr, n):
        for i in xrange(n):
            if check(row[i:i+4]):
                return True

    # Check rows
    n = len(matr) - 3
    for row in matr:
        if check2(row, n):
            return True
    # Check cols
    l = zip(*matr)
    for row in l:
        if check2(row, n):
            return True

    # Check diagonals
    for i in xrange(n):
        for j in xrange(n):
            row = [matr[i+k][j+k] for k in xrange(4)]
            if check(row):
                return True

    m = len(matr)
    for i in xrange(n):
        for j in xrange(n):
            row = [matr[i+k][m-1-j-k] for k in xrange(4)]
            if check(row):
                return True
            

    return False

if __name__ == '__main__':
    assert checkio([
        [1, 1, 1, 1],
        [1, 2, 3, 4],
        [5, 4, 3, 1],
        [6, 1, 3, 2]
    ]) == True, "First, horizontal"
    assert checkio([
        [7, 6,  5, 7, 9],
        [8, 7,  3, 6, 5],
        [4, 0,  6, 5, 4],
        [9, 8,  4, 0, 5],
        [2, 10, 7, 2, 10]
    ]) == False, "Second"
    assert checkio([
        [10, 1, 9,  6, 4, 1],
        [2,  5, 4,  2, 2, 7],
        [2,  2, 1,  2, 6, 4],
        [3,  2, 2,  1, 0, 2],
        [7,  9, 6,  2, 5, 7],
        [7,  3, 10, 5, 6, 2]
    ]) == True, "Third"
    assert checkio([
        [6, 6, 7, 7, 7],
        [1, 7, 3, 6, 5],
        [4, 1, 2, 3, 2],
        [9, 0, 4, 0, 5],
        [2, 0, 7, 5, 10]
    ]) == False, "fourth"
    assert checkio([
        [1,  1, 1,  6, 1, 1, 1],
        [2,  5, 4,  2, 2, 7, 2],
        [2,  6, 1,  2, 6, 4, 3],
        [3,  2, 2,  1, 0, 2, 4],
        [7,  9, 6,  2, 5, 7, 5],
        [7,  3, 10, 5, 6, 2, 5],
        [7,  3, 10, 5, 6, 2, 5]
    ]) == False, "Fifth"
    assert checkio([
        [1, 1, 3, 1],
        [1, 2, 3, 4],
        [5, 4, 3, 1],
        [6, 1, 3, 2]
    ]) == True, "Six, vertircal"
