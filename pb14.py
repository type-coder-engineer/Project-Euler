#coding: utf
import math
import time

def rules(input):
    return (input / 2) if input % 2 == 0 else (3 * input + 1)
        
def nb_sequence(nb):
    index = 1
    while(nb != 1):
        nb = rules(nb)
        index += 1
    return index

def solve():
    test = 2
    max = 0
    max_nb = 0
    while(test < 1000000):
        print test
        sum = nb_sequence(test)
        if sum > max:
            max = sum
            max_nb = test
        else:
            pass
        test += 1
    return max_nb
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)

