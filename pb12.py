#coding: utf
import math
import time

def nb_factors(nb):
    factors = 0
    for i in range(1, nb + 1):
        if nb % i == 0:
            factors += 1
        else:
            pass
    return factors
    
def triangle_numbers():
    index = 1
    while(1):
        sum = 0
        for i in range(1, index + 1):
            sum += i
        # print sum
        # raw_input()
        yield sum
        index += 1
    return 
    
def solve():
    for nb in triangle_numbers():
        if nb_factors(nb) >= 500:
            return nb
        else:
            pass
    
if __name__ == '__main__':
    start = time.time()
    print 'the answer is {}'.format(solve()) 
    end = time.time()
    print 'it took {} seconds'.format(end - start)