#coding: utf
import time

def solve():
    # sum = 0
    # for i in xrange(1, 1001):
        # print i
        # sum += i**i
    # return str(sum)[-10:]
    return str(sum(i**i for i in xrange(1, 1001)))[-10:]
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)