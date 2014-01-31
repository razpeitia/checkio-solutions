def checkio(offers):
    '''
       the amount of money that Petr will pay for the ride
    '''
    initial_petr, raise_petr, initial_driver, reduction_driver = offers
    i = 0
    while True:
        a = initial_petr + (raise_petr * i)
        b = initial_driver - (reduction_driver * i)
        i += 1
        if a >= b:
            return a
        if a + raise_petr >= b:
            return b


if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    print 'All is ok'
    
    
