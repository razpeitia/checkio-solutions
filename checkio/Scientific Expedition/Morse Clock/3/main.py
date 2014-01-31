def checkio(data):
    
    def to_morse(digit, width):
        return bin(digit)[2:2+width].zfill(width).replace('0', '.').replace('1', '-')
        
    h, m, s = map(int, data.split(":"))
    
    h1, h2 = (h // 10) % 10, h % 10
    m1, m2 = (m // 10) % 10, m % 10
    s1, s2 = (s // 10) % 10, s % 10
    
    h1, h2 = to_morse(h1, 2), to_morse(h2, 4)
    m1, m2 = to_morse(m1, 3), to_morse(m2, 4)
    s1, s2 = to_morse(s1, 3), to_morse(s2, 4)
    
    return "%s %s : %s %s : %s %s" % (h1, h2, m1, m2, s1, s2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"


