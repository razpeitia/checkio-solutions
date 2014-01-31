from math import acos, degrees

def checkio(a, b, c):
    a, b, c = sorted([a, b, c])
    if a + b > c:
        c_ = degrees(acos((a*a + b*b - c*c) / float(2 * a * b)))
        b_ = degrees(acos((a*a + c*c - b*b) / float(2 * a * c)))
        a_ = degrees(acos((b*b + c*c - a*a) / float(2 * b * c)))
        a_, b_, c_ = round(a_), round(b_), round(c_)
        return sorted((a_, b_, c_))
    else:
        return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
