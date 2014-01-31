from fractions import gcd

def reduce_fraction(a, b):
    c = gcd(a, b)
    a, b = a / c, b / c
    return a, b

def count_multiples(n, m):
    i = 0
    while n % m == 0:
        n /= m
        i += 1
    return i

def decimals(a, b):
    a, b = reduce_fraction(a, b)
    r = a % b
    q = a / b
    l = [q]
    path = set([r])
    while True:
        q = (r * 10) / b
        r = (r * 10) % b
        l.append(q)
        if r == 0 or r in path: break
        path.add(r)
    return l

def repeting_decimals(a, b):
    a, b = reduce_fraction(a, b)
    dec = map(str, decimals(a, b))

    start_digits = max(count_multiples(b, 2), count_multiples(b, 5))

    integer = dec[0]
    start = ''.join(dec[1:1+start_digits])
    repeting = ''.join(dec[1+start_digits:])

    if repeting:
        s = '%s.%s(%s)' % (integer, start, repeting)
    else:
        s = '%s.%s' % (integer, start)
    return s

def checkio(fraction):
    numerator, denominator = fraction

    return repeting_decimals(numerator, denominator)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 3]) == "0.(3)", "1/3 Classic"
    assert checkio([5, 3]) == "1.(6)", "5/3 The same, but bigger"
    assert checkio([3, 8]) == "0.375", "3/8 without repeating part"
    assert checkio([7, 11]) == "0.(63)", "7/11 prime/prime"
    assert checkio([29, 12]) == "2.41(6)", "29/12 not and repeating part"
    assert checkio([11, 7]) == "1.(571428)", "11/7 six digits"

