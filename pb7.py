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
    
def solve():
    index = 2
    index_prime = 0
    while(1):
        if is_prime(index):
            index_prime += 1
        else:
            pass
        if index_prime == 10001:
            return index
        index += 1
        
if __name__ == '__main__':
    start = time.time()
    print 'the answer is {}'.format(solve()) 
    end = time.time()
    print 'it took {} seconds'.format(end - start)