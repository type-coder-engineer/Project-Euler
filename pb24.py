#coding: utf
import time
import itertools

# def solve():
    # index = 0
    # for one in itertools.permutations(range(10)):
        # index += 1
        # if index == 1000000:
            # return one
        # else:
            # pass
    # return 'no answer'

def myPermutations(iterable, r = None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    print tuple(pool[i] for i in indices[:r])
    # raw_input()
    while n:
        for i in reversed(range(r)):
            print i
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
                print indices
                print 'no res'
                print '*********'
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                print indices
                print tuple(pool[i] for i in indices[:r])
                print '*********'
                break
        else:
            return
    

if __name__ == '__main__':
    start = time.time()
    # print "The answer is {}".format(solve())
    myPermutations('123', 3)
    end = time.time()
    print "it took {} seconds".format(end - start)