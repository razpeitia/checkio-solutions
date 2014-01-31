def checkio(stair_values):
    def f(l, i, s):
        n = len(l)
        if i >= n: return s

        a = l[i]
        try:
            b = l[i + 1]
        except IndexError:
            b = 0

        return max(
            f(l, i + 1, s + a),
            f(l, i + 2, s + b)
        )

    return f(stair_values, 0, 0)

        

if __name__ == '__main__':
   assert checkio([5,6,-10,-7,4]) == 8, 'First'
   assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95])==393, 'Second'
   assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27])==125, 'Third'
   assert checkio([5,-3,-1,2]) == 6, 'Fifth'
   print('All ok')
