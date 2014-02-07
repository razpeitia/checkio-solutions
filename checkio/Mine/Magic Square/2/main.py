def is_valid(data):
    n = len(data)
    rows = [sum(row) for row in data]
    cols = [sum(col) for col in zip(*data)]
    diag = [
        sum(data[i][i] for i in range(n)), 
        sum(data[i][n-i-1] for i in range(n)),
    ]
    return set(rows + cols + diag) == set([n * (n * n + 1) / 2])

def should_continue(data):
    n = len(data)
    M = n * (n * n + 1) / 2
    return all(sum(row) <= M for row in data) and \
            all(sum(col) <= M for col in zip(*data)) and \
            sum(data[i][i] for i in range(n)) <= M and \
            sum(data[i][n-i-1] for i in range(n)) <= M       

def get_candidate(data):
    n = len(data)
    ni, nj = None, None
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                ni, nj = i, j
                break
        if ni is not None: break
    return [(ni, nj, x) for x in set(range(1, n * n + 1)) - set(sum(data, [])) - set([0])]

def backtrack(data):
    if not should_continue(data):
        return None
    if is_valid(data):
        return data
    candidate = get_candidate(data)
    for i, j, c in candidate:
        data[i][j] = c
        r = backtrack(data)
        if r is not None:
            return r
        data[i][j] = 0

def checkio(data):
    return backtrack(data)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 0]
    ]))
    #must return [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

    print(checkio([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]))

    print(checkio([
        [0, 0, 0],
        [0, 5, 0],
        [0, 0, 0]
    ]))
    #can return [[2, 7, 6], [9, 5, 1], [4, 3, 8]] or
    # [[4, 9, 2], [3, 5, 7], [8, 1, 6]

    print(checkio([[1, 15, 14, 4],
                   [12, 0, 0, 9],
                   [8, 0, 0, 5],
                   [13, 3, 2, 16]]))
    # answer [[1, 15, 14, 4], [12, 6, 7, 9], [8, 10, 11, 5], [13, 3, 2, 16]]
