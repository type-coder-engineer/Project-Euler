#coding: utf
import time

def solve():
    n = 1
    while(1):
        if verify(n):
            return n
        else:
            n += 1

def verify(n):
    digits = list(str(n))
    digits.sort()
    for time in xrange(2, 7):
        new_digits = list(str(time*n))
        new_digits.sort()
        if digits != new_digits:
            return False
        else:
            pass
    return True
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)