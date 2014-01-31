def checkio(matr):
    '''
    Given matrix  NxN (3<=N<=10). 
    Numbers between 1 and 5 are elements of A. 
    Find the biggest union of the same numbers in group and the number. 
    Say, group is a bunch of numbers that stay near each other.
    '''
    n = len(matr)
    m = len(matr[0])
    l = [[1] * m for i in xrange(n)]
    def flood(arr, l, x, y, target, count):
        l[x][y] = 0
        if (x + 1) < len(arr) and l[x+1][y] and arr[x+1][y] == target:
            count = flood(arr, l, x + 1, y, target, count + 1)

        if (x - 1) >= 0 and l[x-1][y] and arr[x-1][y] == target:
            count = flood(arr, l, x - 1, y, target, count + 1)

        if (y + 1) < len(arr[0]) and l[x][y+1] and arr[x][y+1] == target:
            count = flood(arr, l, x, y + 1, target, count + 1)

        if (y - 1) >= 0 and l[x][y-1] and arr[x][y-1] == target:
            count = flood(arr, l, x, y - 1, target, count + 1)

        return count

    ans = []
    for i in xrange(n):
        for j in xrange(m):
            if l[i][j]:
                c = flood(matr, l, i, j, matr[i][j], 1)
                ans.append([c, matr[i][j]])
    s = max(ans)
    return s

if __name__ == '__main__':
    assert checkio([
        [1,2,3,4,5],
        [1,1,1,2,3],
        [1,1,1,2,2],
        [1,2,2,2,1],
        [1,1,1,1,1]
    ])==[14,1], 'First'

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ])==[19,2], 'Second'

    print 'All ok'
