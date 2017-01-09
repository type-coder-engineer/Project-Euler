#coding: utf
import math
import sys
import time

def solve():
    total_square = 0
    total_sum = 0
    for i in range(1, 101):
        total_square += i**2
        total_sum += i
    return total_sum**2 - total_square
    
if __name__ == '__main__':
    start = time.time()
    print 'the answer is {}'.format(solve()) 
    end = time.time()
    print 'it took {} seconds'.format(end - start)