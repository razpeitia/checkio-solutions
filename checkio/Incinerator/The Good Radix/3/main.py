def checkio(number):
    for k in range(2, 37):
        try:
            n = int(number, k)
            if n % (k - 1) == 0:
                return k
        except:
            pass
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    print('Local tests done')

