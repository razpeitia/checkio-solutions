c = 0
def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    w = sum(stones) / 2
    items = stones
    global c
    c = 0
    def ks(index, weight):
        global c
        c += 1

        if index >= len(items):
            return 0

        item = items[index]

        if item > weight:
            return ks(index + 1, weight)
        else:
            return max(ks(index + 1, weight),
                       ks(index + 1, weight - item) + item)
    a = ks(0, w)
    b = sum(stones)
    return b - (a * 2)


if __name__ == '__main__':
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print 'All is ok'
