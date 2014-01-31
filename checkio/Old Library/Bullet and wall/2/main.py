def checkio(data):
    xw1, yw1 = data[0]
    xw2, yw2 = data[1]

    xa, ya = data[2]
    xb, yb = data[3]

    A1 = yw2 - yw1
    B1 = xw1 - xw2
    C1 = A1 * xw1 + B1 * yw1

    A2 = yb - ya
    B2 = xa - xb
    C2 = A2 * xa + B2 * ya

    det = A1 * B2 - A2 * B1
    if det == 0:
        if C1 == C2:
            x1 = (xa <= xb and xw1 >= xa) or (xa >= xb and xw1 <= xa)
            y1 = (ya <= yb and yw1 >= ya) or (ya >= yb and yw1 <= ya)
            x2 = (xa <= xb and xw2 >= xa) or (xa >= xb and xw2 <= xa)
            y2 = (ya <= yb and yw2 >= ya) or (ya >= yb and yw2 <= ya)
            return (x1 and y1) or (x2 and y2)
        else:
            return False
    else:
        x = float(B2 * C1 - B1 * C2) / det
        y = float(A1 * C2 - A2 * C1) / det
        
        if xw1 > xw2:
            xw2, xw1 = xw1, xw2
        if yw1 > yw2:
            yw2, yw1 = yw1, yw2
        
        c = (xw1 <= x <= xw2) and (yw1 <= y <= yw2)
        x = (xa <= xb and x >= xa) or (xa >= xb and x <= xa)
        y = (ya <= yb and y >= ya) or (ya >= yb and y <= ya)
        return c and x and y
            


if __name__ == '__main__':
    assert checkio([[0,0], [0,2], [5,1], [3,1]]) == True, "First"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "Reverse First"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "Second"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "Third"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "Fourth, shot in butt of wall :)"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "Fifth, parallel"
    assert checkio([[2, 4], [2, 0], [0, 2], [2, 3]]) == True, "Sixth, Vertical wall"
