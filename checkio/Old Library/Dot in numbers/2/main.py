import re

def checkio(txt):
    '''
    string with dot separated numbers, which inserted after every third digit from right to left
    '''
    def chunks(l, n):
        """ Yield successive n-sized chunks from l.
        """
        for i in xrange(0, len(l), n):
            yield l[i:i+n]

    p = re.compile(r"(\d{4,})(?![tT][hH])")
    s = p.search(txt)
    if s:
        ans = txt
        while s:
            x, y = s.span()
            num = ans[x:y]
            num = num[::-1]
            num = '.'.join(list(chunks(num, 3)))
            num = num[::-1]
            ans = ans[:x] + num + ans[y:]
            s = p.search(ans)
        return ans
    else:
        return txt

if __name__ == '__main__':
    assert checkio('123456') == '123.456'
    assert checkio('333') == '333'
    assert checkio('9999999') == '9.999.999'
    assert checkio('123456 567890') == '123.456 567.890'
    assert checkio('price is 5799') == 'price is 5.799'
    assert checkio('he was born in 1966th') == 'he was born in 1966th'
    print 'All ok'
