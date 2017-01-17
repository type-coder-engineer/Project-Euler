#coding: utf
import time
import itertools

def solve():
    index = 0
    for one in itertools.permutations(range(10)):
        index += 1
        if index == 1000000:
            return one
        else:
            pass
    return 'no answer'
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)