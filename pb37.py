#coding: utf
import time
import math

def solve():
    sum = 0
    index = 0
    nb = 11
    while(1):
        if isTruncatable(str(nb)):
            index += 1
            sum += nb
            if index == 11:
                return sum
        else:
            pass
        nb += 1
        
def isTruncatable(nb):
    length = len(nb)
    for i in range(length):
        if isPrime(int(nb[i:])) and isPrime(int(nb[:length - i])):
            continue 
        else:
            return False
    return True

def isPrime(nb):
    if nb > 1:
        if nb == 2:
            return True
        elif nb % 2 == 0:
            return False
        for possible in range(3, int(math.sqrt(nb) + 1), 2):
            if nb % possible == 0:
                return False
        return True
    return False
    
if __name__ == '__main__':
    start = time.time()
    # print isTruncatable('377')
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)