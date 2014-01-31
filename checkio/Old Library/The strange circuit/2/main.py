def spiral(n):
    dx, dy = 1, 0            # Starting increments
    x, y = 0, 0              # Starting location
    myarray = [[None] * n for j in xrange(n)]
    c = n * n
    for i in xrange(c):
        myarray[x][y] = c - i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return myarray

def get_adj(x, y):
    global n
    def g(x, y):
        yield x + 1, y
        yield x - 1, y
        yield x, y + 1
        yield x, y - 1
    for i, j in g(x, y):
        if (0 <= i < n) and (0 <= j < n):
            yield i, j

def bfs(arr, x, y, target):
    visited = set()
    queue = [(0, x, y)]
    while queue:
        c, x, y = queue.pop(0)
        visited.add((x, y))
        if arr[x][y] == target:
            return c
        for i, j in get_adj(x, y):
            if (i, j) not in visited:
                visited.add((i, j))
                queue.append((c + 1, i, j))

n = 33
l = spiral(n)

def checkio(data):
    "Find the destination"
    global l
    global n
    a, b = data
    for i, row in enumerate(l):
        for j, data in enumerate(row):
            if a == data:
                x = bfs(l, i, j, b)
                return x

if __name__ == '__main__':
    assert checkio([1, 9]) == 2, "First"
    assert checkio([9, 1]) == 2, "Reverse First"
    assert checkio([10, 25]) == 1, "Neighbours"
    assert checkio([5, 9]) == 4, "Diagonal"
    assert checkio([26, 31]) == 5, "One row"
    assert checkio([50, 16]) == 10, "One more test"
