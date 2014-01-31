import re

def checkio(data):
    'Return True if password strong and False if not'
    return bool(len(data) >= 10 and re.search('[0-9]', data) and re.search('[a-z]', data) and re.search('[A-Z]', data))

if __name__ == '__main__':
    assert checkio('A1213pokl')==False, 'First'
    assert checkio('bAse730onE4')==True, 'Second'
    assert checkio('asasasasasasasaas')==False, 'Third'
    assert checkio('QWERTYqwerty')==False, 'Fourth'
    assert checkio('123456123456')==False, 'Fifth'
    assert checkio('QwErTy911poqqqq')==True, 'Sixth'
    print 'All ok'
