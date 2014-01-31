class Point(object):
    def __init__(self, _id, line=None):
        self.id = _id
        
        # Get line
        if line is None:
            n = 1
            while n * (n + 1) / 2 < self.id:
                n += 1
            self.line = n
        else:
            self.line = line

    def __eq__(self, point):
        return self.id == point.id

    def __cmp__(self, point):
        return cmp(self.id, point.id)

    def left(self):
        return Point(self.id + self.line, line=self.line+1)

    def right(self):
        return Point(self.id + self.line + 1, line=self.line+1)

    def is_right(self, point):
        if self.in_same_line(point):
            return False
        if self.line < point.line:
            right = self.right()
            target = point
        else:
            right = point.right()
            target = self
        while True:
            if right == target:
                return True
            elif right > target:
                break
            right = right.right()
        return False

    def is_left(self, point):
        if self.in_same_line(point):
            return False
        if self.line < point.line:
            left = self.left()
            target = point
        else:
            left = point.left()
            target = self
        while True:
            if left == target:
                return True
            elif left > target:
                break
            left = left.left()
        return False

    def in_same_line(self, point):
        return self.line == point.line

    def distance(self, point):
        if self.in_same_line(point):
            return abs(self.id - point.id)
        elif self.is_right(point) or self.is_left(point):
            return abs(self.line - point.line)

    def __str__(self):
        return "(%d :%d)" % (self.id, self.line)


def checkio(inset):
    n = len(inset)
    if n == 3:
        inset = [Point(p) for p in inset]
        inset.sort()

        a, b, c = inset
        if a.distance(b) == b.distance(c) and a.distance(c) == b.distance(c):
            p = a.in_same_line(b)
            q = c.in_same_line(b)
            if p ^ q:
                return 3
            else:
                return 0
        else:
            return 0
    elif n == 4:
        inset = [Point(p) for p in inset]
        inset.sort()

        a, b, c, d = inset
        ab = a.distance(b)
        cd = c.distance(d)
        ac = a.distance(c)
        bd = b.distance(d)
        _ab = a.in_same_line(b)
        _cd = c.in_same_line(d)
        if (ab == cd == ac == bd) and _ab and _cd:
            return 4
        else:
            return 0
    elif n == 6:
        inset = [Point(p) for p in inset]
        inset.sort()

        a, b, c, d, e, f = inset
        _ab = a.in_same_line(b)
        _cd = c.in_same_line(d)
        _ef = e.in_same_line(f)
        if _ab and _cd and _ef:
            ab = a.distance(b)
            ac = a.distance(c)
            bd = b.distance(d)
            ce = c.distance(e)
            df = d.distance(f)
            ef = e.distance(f)
            if ab == ac == bd == ce == df == ef:
                return 6
            else:
                return 0
        else:
            return 0
    else:
        return 0

if __name__ == "__main__":
    assert checkio([1,2,3]) == 3, 'triangle'
    assert checkio([11,13,29,31]) == 0, 'not parallelogram'
    assert checkio([26,11,13,24]) == 4, 'parallelogram'
    assert checkio([4,5,9,13,12,7]) == 6, 'hexagon'
    assert checkio([1,2,3,4,5]) == 0, 'it very strange triangle'
    assert checkio([47]) == 0, 'point'
    assert checkio([11,13,23,25]) == 0, 'again not parallelogram'
