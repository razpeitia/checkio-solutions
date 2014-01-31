def checkio(data):
    A, B, C, N = data
    """Shameless solution"""
    count = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if (a + b + c) <= N:
                    count += 1
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([3, 2, 1, 4]) == 20, "First example"
    assert checkio([1, 1, 1, 1]) == 4, "Second example"

