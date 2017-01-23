#coding: utf
import time

# Since 9^5 * 7 < 10^6, the number has at most 6 digits.
def solve():
    res = 0
    for index in range(2, 1000000):
        if index == sum(int(one)**5 for one in str(index)):
            print index
            res += index
        else:
            pass
    return res
            
if __name__ == '__main__':
	start = time.time()
	print 'The answer is {}'.format(solve())
	end = time.time()
	print "It took {} seconds".format(end - start)