#coding: utf
import time
import math
import itertools

def solve():
    nb = 0
    for index in range(2, 1000001):
        if isCircularPrime(index):
            nb += 1
        else:
            pass
    return nb
 
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
    
def isCircularPrime(nb):
    string_nb = str(nb)
    for index in range(len(string_nb)):
        new_nb = ''
        for i in range(len(string_nb)):
            new = i + index if i + index < len(string_nb) else i + index - len(string_nb)
            new_nb += string_nb[new]
        if is_prime(int(new_nb)):
            continue
        else:
            return False
    return True
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)