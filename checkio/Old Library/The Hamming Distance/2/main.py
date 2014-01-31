def checkio(data):
    a, b = data
    c = a ^ b
    return bin(c).count('1')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([117, 17]) == 3, "First example"
    assert checkio([1, 2]) == 2, "Second example"
    assert checkio([16, 15]) == 5, "Third example"

