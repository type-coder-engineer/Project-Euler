#coding: utf
import time
import itertools
import math

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
    
def list_prime():
    n = 1001
    list = []
    while(n < 10000):
        if isPrime(n):
            list.append(n)
        n += 1
    return list

def verify(a, b, c):
    if b - a != c - b:
        return False
    else:
        list_a = list(str(a))
        list_b = list(str(b))
        list_c = list(str(c))
        list_a.sort()
        list_b.sort()
        list_c.sort()
        if list_a == list_b == list_c:
            return True
        else:
            return False
            
def solve(list):
    length = len(list)
    for combination in itertools.combinations(xrange(length), 3):
        if verify(list[combination[0]], list[combination[1]], list[combination[2]]):
            if list[combination[0]] == 1487 and list[combination[1]] == 4817:
                pass
            else:
                return str(list[combination[0]]) +  str(list[combination[1]]) + str(list[combination[2]])

if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve(list_prime()))
    end = time.time()
    print "it took {} seconds".format(end - start)

