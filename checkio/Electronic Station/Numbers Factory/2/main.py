def checkio(data):

    if data < 10: return data
    
    i = 2
    l = []
    while i*i <= data:
        while data % i == 0:
            data /= i
            l.append(i)
        i += 1
    if data != 1:
        l.append(data)
    if len(l) == 1 or any(i > 10 for i in l):
        return 0
    
    t = 0
    ans = []
    for i in l:
        if t == 0:
            t = i
        elif (t * i) < 10:
            t *= i
        else:
            ans.append(t)
            t = i
    if t:
        ans.append(t)
    ans.sort()
    return int(''.join(str(i) for i in ans))
            
        

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"

