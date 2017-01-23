#coding: utf
import time

def solve():
    res = 1
    current_nb = 1
    for step in range(2, 1001, 2):
        for time in range(0,4):
            current_nb += step
            res += current_nb
    return res
            
if __name__ == '__main__':
	start = time.time()
	print 'The answer is {}'.format(solve())
	end = time.time()
	print "It took {} seconds".format(end - start)