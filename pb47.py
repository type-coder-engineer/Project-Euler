#coding: utf
import time, math

def solve():
    flag_nb = 0
    n = 647
    while(1):
        # print n
        allFactors = factors(n)
        flag = True
        if len(allFactors) == 4:
            for one in allFactors:
                if not isPrime(one):
                    flag = False
                    break
        else:
            flag = False
        if flag:
            flag_nb += 1
        else:
            flag_nb = 0
        if flag_nb == 4:
            return (n - 3)
        else:
            n += 1
    
def factors(n):
    possible = 2
    factors = []
    while(n != 1):
        if n % possible == 0:
            n /= possible
            factors.append(possible)
        else:
            possible += 1
    factors = list(set(factors))
    return factors
    
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
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)