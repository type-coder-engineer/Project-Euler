#coding: utf
import time, math

def combinatoric_nb(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)
    
def solve():
    res = 0
    for n in xrange(1, 101):
        for r in xrange(1, n + 1):
            if combinatoric_nb(n, r) > 1000000:
                res += 1
    return res

if __name__ == '__main__':
    start = time.time()
    # print combinatoric_nb(23, 10)
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)