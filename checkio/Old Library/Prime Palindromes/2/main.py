#Your code here
#You can import some modules or create additional functions


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    def is_palindrome(num):
        num = str(num)
        return num == num[::-1]
        
    def is_prime(num):
        sq_num = int(num ** .5) + 1
        if (num & 1) == 0: return False
        for i in xrange(3, sq_num + 1, 2):
            if num % i == 0: return False
        return True

    num = data
    while True:
        if is_palindrome(num) and is_prime(num):
            return num
        num += 1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(31) == 101, 'First example'
    assert checkio(130) == 131, 'Second example'
    assert checkio(131) == 131, 'Third example'
