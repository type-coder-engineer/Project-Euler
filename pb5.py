#coding: utf
import math
import sys
import time

def solve():
    test_nb = step
    while(test_nb <= sys.maxint):
        flag_ok = True
        for one in test_range:
            if test_nb % one == 0:
                pass
            else:
                flag_ok = False
                break
        if flag_ok == True:
            return test_nb
        else:
            test_nb += step
    return 'not found one, the test number is bigger than the max int ...'
    
if __name__ == '__main__':
    step = 3*5*7*11*13*17*19
    test_range = [16,18,20]
    start = time.time()
    print 'the answer is {}'.format(solve()) 
    end = time.time()
    print 'it took {} seconds'.format(end - start)