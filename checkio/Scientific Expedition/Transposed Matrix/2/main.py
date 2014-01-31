def checkio(matr):
    'return a transposed matrix'
    a = len(matr)
    b = len(matr[0])
    l = [[0] * a for i in xrange(b)]
    for i in xrange(a):
        for j in xrange(b):
            l[j][i] = matr[i][j]
    return l
    
    
if __name__ == '__main__':
    assert checkio([[1,2],
             [1,2]]) ==  [[1, 1],
                          [2, 2]], 'First'
    assert checkio([[1,0,3,4,0],
                    [2,0,4,5,6],
                    [3,4,9,0,6]]) == [[1, 2, 3],
                                      [0, 0, 4],
                                      [3, 4, 9],
                                      [4, 5, 0],
                                      [0, 6, 6]],'Second'
    print 'All ok'
