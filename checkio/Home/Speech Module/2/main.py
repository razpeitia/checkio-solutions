def checkio(number):
    n = number
    d = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        # 21 - twenty-one
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred'
    }
    
    def f(n):
        if n <= 20:
            return d[n]

        a = (n / 10) * 10
        b = n % 10
        if b == 0:
            return "{0}".format(d[a])
        else:
            return "{0} {1}".format(d[a], d[b])
    if n < 100:
        return f(n)
    else:
        a = (n / 100) % 10
        b = n % 100
        if b == 0:
            return "{0} {1}".format(d[a], d[100])
        else:
            return "{0} {1} {2}".format(d[a], d[100], f(b))

if __name__ == '__main__':
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)=='twelve', "Third"
    assert checkio(101)=='one hundred one', "Fifth"
    assert checkio(212)=='two hundred twelve', "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"

    print 'All ok'
