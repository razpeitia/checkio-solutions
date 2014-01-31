def checkio(number):
    'return roman numeral using the specified integer value from range 1...3999'
    d = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        
        10: 'X',
        20: 'XX',
        30: 'XXX',
        40: 'XL',
        50: 'L',
        60: 'LX',
        70: 'LXX',
        80: 'LXXX',
        90: 'XC',

        100: 'C',
        200: 'CC',
        300: 'CCC',
        400: 'CD',
        500: 'D',
        600: 'DC',
        700: 'DCC',
        800: 'DCCC',
        900: 'CM',
        
        1000: 'M',
        2000: 'MM',
        3000: 'MMM',
        }
    n = number
    ans = []
    i = 0
    while n:
        a = (n % 10) * (10 ** i)
        if not (i == 0 and a == 0):
            ans.append(d[a])
        n /= 10
        i += 1
    ans = ans[::-1]
    ans = ''.join(ans)
    return ans
    
if __name__ == '__main__':
    assert checkio(6) == 'VI', 'First'
    assert checkio(76) == 'LXXVI', 'Second'
    assert checkio(499) == 'CDXCIX', 'Third'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', 'Fourth'
    print 'All ok'
