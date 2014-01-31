def checkio(lines_list):
    """Return the qantity of squares"""
    d = set()
    for a, b in lines_list:
        if a > b:
            a, b = b, a
        d.add((a, b))

    def get_square(n, sz):
        return (n, n + sz, n + (4 * sz), n + (5 * sz))

    def get_all_lines(square):
        tl, tr, bl, br = square
        top = [(i, i + 1) for i in xrange(tl, tr)]
        left = [(i, i + 4) for i in xrange(tl, bl, 4)]
        rigth = [(i, i + 4) for i in xrange(tr, br, 4)]
        bottom = [(i, i + 1) for i in xrange(bl, br)]
        return set(top) | set(left) | set(rigth) | set(bottom)


    l = [
        get_all_lines(get_square(1, 1)),
        get_all_lines(get_square(2, 1)),
        get_all_lines(get_square(3, 1)),
        get_all_lines(get_square(5, 1)),
        get_all_lines(get_square(6, 1)),
        get_all_lines(get_square(7, 1)),
        get_all_lines(get_square(9, 1)),
        get_all_lines(get_square(10, 1)),
        get_all_lines(get_square(11, 1)),


        get_all_lines(get_square(1, 2)),
        get_all_lines(get_square(2, 2)),
        get_all_lines(get_square(5, 2)),
        get_all_lines(get_square(6, 2)),

        get_all_lines(get_square(1, 3)),
    ]

    c = 0
    for i in l:
        if i <= d:
            c += 1
    return c

if __name__ == '__main__':
    assert (checkio([[1,2],[3,4],[1,5],[2,6],[4,8],[5,6],[6,7],
                     [7,8],[6,10],[7,11],[8,12],[10,11],
                     [10,14],[12,16],[14,15],[15,16]]) == 3) , "First, from description"
    assert (checkio([[1,2],[2,3],[3,4],[1,5],[4,8],
                     [6,7],[5,9],[6,10],[7,11],[8,12],
                     [9,13],[10,11],[12,16],[13,14],[14,15],[15,16]]) == 2), "Second, from description"
    assert (checkio([[1,2], [1,5], [2,6], [5,6]]) == 1), "Third, one small square"
    assert (checkio([[1,2], [1,5], [2,6], [5,9], [6,10], [9,10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16,15], [16,12], [15,11], [11,10],
                     [10,14], [14,13], [13,9]]) == 0), "Fifth, snake"
