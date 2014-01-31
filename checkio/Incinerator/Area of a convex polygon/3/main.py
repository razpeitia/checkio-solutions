def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))
def segments(p):
    return zip(p, p[1:] + [p[0]])
    
def checkio(data):
    return area(data)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 1], [9, 9], [9, 1]]) == 32, "The half of the square"
    assert checkio([[4, 10], [7, 1], [1, 4]]) == 22.5, "Triangle"
    assert checkio([[1, 2], [3, 8], [9, 8], [7, 1]]) == 40, "Quadrilateral"
    assert checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]) == 26, "Pentagon"
    assert checkio([[7, 2], [3, 2], [1, 5],
                    [3, 9], [7, 9], [9, 6]]) == 42, "Hexagon"
    assert checkio([[4, 1], [3, 4], [3, 7], [4, 8],
                    [7, 9], [9, 6], [7, 1]]) == 35.5, "Heptagon"

