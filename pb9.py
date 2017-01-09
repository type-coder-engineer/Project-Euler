#coding: utf
import math
import time

def solve():
    a = 1
    b = 1
    while(a < 500 and b < 500):
        if a**2 + b**2 == (1000 - a - b)**2:
            return a*b*(1000 - a - b)
        else:
            pass
        if a < 499:
            a += 1
            continue
        else:
            b += 1
            a = 1
    return 'you are a liar...'
    
if __name__ == '__main__':
    start = time.time()
    print 'the answer is {}'.format(solve()) 
    end = time.time()
    print 'it took {} seconds'.format(end - start)