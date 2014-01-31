from fractions import gcd

def checkio(values):
    'Calculate the greatest common divisor of two numbers'
    a, b = values
    return gcd(a, b)

if __name__ == '__main__':
    assert checkio((12, 8)) == 4, "First"
    assert checkio((14, 21)) == 7, "Second"
    print 'All ok'
    

