#coding: utf
import time
import math

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

def oddComposite():
    n = 8
    while(1):
        if n % 2 == 1 and not is_prime(n):
            yield n
        n += 1

def verify(n):
    test = 1
    while(2*test**2 < n):
        rest = n - 2*test**2
        if is_prime(rest):
            return True
        else:
            test += 1
    return False
    
def solve():
    for one in oddComposite():
        # print one
        # raw_input()
        if not verify(one):
            return one
        else:
            pass
            
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)