#coding: utf
import math
import time

def is_prime(nb):
    if nb > 1:
        if nb == 2:
            return True
        elif nb % 2 == 0:
            return False
        for possible in range(3, int(math.sqrt(nb) + 1), 2):
            if nb % possible == 0:
                return False
        return True
    return False

def get_divisor(nb):
    for i in range(1, nb + 1):
        if nb % i == 0:
            # print i
            yield i
        else:
            pass
    return 

def verify(nb):
    for divisor in get_divisor(nb):
        if is_prime(divisor + nb/divisor):
            pass
        else:
            return False
    return True
    
def sum():
    total = 0
    nb = 1
    while(nb <= 1000000):
        if nb % 10000 == 0:
            print nb / 10000
    # while(nb <= 5):
        if verify(nb):
            total += nb
        else:
            pass
        # print '***********'
        nb += 1
    return total

if __name__ == '__main__':
    start = time.time()
    print sum()
    end = time.time()
    print 'it took {} seconds'.format(end - start)
    # it took us 141.9 seconds to calcul 10,000,000 with pypy, 
    # and 501.2 seconds with swift...
    # and 6276.9 seconds to calcul 1,000,000 with python....what a disappointment of the efficiency of python....
    # remember, to do large simple calculs, please use pypy!!