#coding: utf
import time

def solve():
    max = 0
    for a in range(1, 100):
        for b in range(1, 100):
            mySum = sum(int(one) for one in str(a**b))
            max = mySum if mySum > max else max
    return max

if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)