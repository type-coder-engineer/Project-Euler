#coding: utf
import time

def solve():
    res = 1
    for index in range(2, 10):
        power = 1
        while(1):
            length = len(str(index ** power))
            if length == power:
                res += 1
            if length < power:
                break
            else:
                power += 1
    return res
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)