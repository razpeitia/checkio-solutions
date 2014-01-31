def checkio(data):
    """list[list[int]] -> int
    Return max possible sum in a path from top to bottom
    """
    def get(arr, index, default=0):
        if index < 0: return default
        try:
            return arr[index]
        except IndexError:
            return default
    
    rows = len(data)
    for i in range(1, rows):
        for j, num in enumerate(data[i]):
            data[i][j] += max(get(data[i-1], j), get(data[i-1], j-1))
    return max(data[-1])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1],
        [2, 3],
        [3, 3, 1],
        [3, 1, 5, 4],
        [3, 1, 3, 1, 3],
        [2, 2, 2, 2, 2, 2],
        [5, 6, 4, 5, 6, 4, 3]
    ]) == 23, "First example"
    assert checkio([
        [1],
        [2, 1],
        [1, 2, 1],
        [1, 2, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 2, 1, 1, 1, 1],
        [1, 2, 1, 1, 1, 1, 9]
    ]) == 15, "Second example"
    assert checkio([
        [9],
        [2, 2],
        [3, 3, 3],
        [4, 4, 4, 4]
    ]) == 18, "Third example"

