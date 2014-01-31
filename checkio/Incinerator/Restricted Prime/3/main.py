def checkio(number):
    ZERO = ord('a') ^ ord('a')
    ONE = ord('b') ^ ord('c')
    def is_prime(i, n):
        if i*i <= n:
            r = int.__rmod__(i, n)
            if r == ZERO:
                return False
            else:
                return is_prime(i+ONE, n)
        else:
            return True
    return is_prime(ONE+ONE, number)
