from string import ascii_uppercase, digits

def convert(character):
    if character.isdigit():
        return int(character)
    else:
        return ord(character) - 48

def sanitize(data):
    return ''.join(c for c in data if c.isalnum())

def mapping(character):
    d = convert(character)
    d *= 2
    if d > 9:
        d = sum(int(c) for c in str(d))
        
    return d

lookup = { c: mapping(c) for c in (digits+ascii_uppercase) }

for k, v in lookup.items():
    if v > 9:
        print(k, v)

def get_ans(data):
    ans = 0
    l = []
    for i, c in enumerate(reversed(data)):
        if not i & 1:
            x = lookup[c]
        else:
            x = convert(c)
        l.append(x)
        ans += x
    print(l)
    d = str((10 - (ans % 10)) % 10)
    return [d, ans]

def checkio(data):
    data = sanitize(data)
    ans = get_ans(data)
    print(ans)
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")

