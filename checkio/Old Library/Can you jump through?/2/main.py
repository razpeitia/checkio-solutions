def checkio(params):
    matr, point1, point2 = params
    n = len(matr)
    x1, y1 = point1
    x2, y2 = point2
    v = [[0] * n for i in xrange(n)]
    c = [False]
    def flood_fill(src_x, src_y):
        v[src_x][src_y] = 1
        if (src_x, src_y) == (x2-1, y2-1):
            c[0] = True

        if src_x + 1 < n and matr[src_x + 1][src_y] == 0 and v[src_x + 1][src_y] == 0:
            flood_fill(src_x + 1, src_y)
        if src_x - 1 >= 0 and matr[src_x - 1][src_y] == 0 and v[src_x - 1][src_y] == 0:
            flood_fill(src_x - 1, src_y)
        if src_y + 1 < n and matr[src_x][src_y + 1] == 0 and v[src_x][src_y + 1] == 0:
            flood_fill(src_x, src_y + 1)
        if src_y - 1 >= 0 and matr[src_x][src_y - 1] == 0 and v[src_x][src_y - 1] == 0:
            flood_fill(src_x, src_y - 1)
    flood_fill(x1-1, y1-1)
    return c[0]
    
    
if __name__ == '__main__':
    assert checkio(([
        [0, 0, 5, 4, 0], 
        [0, 1, 5, 0, 0], 
        [0, 0, 0, 7, 2], 
        [8, 0, 0, 0, 0], 
        [0, 9, 0, 1, 0]], 
        [1,1], [5,3])) == True, 'First'
        
    assert checkio(([
        [0, 0, 5, 4, 0], 
        [0, 1, 5, 0, 0], 
        [0, 0, 0, 7, 2], 
        [8, 0, 0, 0, 0], 
        [0, 9, 0, 1, 0]], 
        [1,1], [1,5])) == False, 'Second'
    
    print 'All ok'
