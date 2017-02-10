#coding: utf
import time
import math, itertools

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

def verify(string):
    digits = len(string)
    for i in xrange(1, digits):
        for change in itertools.combinations(range(digits), i):
            flag = True
            res = []
            nb = string
            count = 0
            if 0 not in change:
                for k in range(10):
                    for digit in change:
                        list_nb = list(nb)
                        list_nb[digit] = str(k)
                        nb = ''.join(list_nb)
                    res.append(nb)
                    if not isPrime(int(nb)):
                        count += 1
                    if count == 3:
                        flag = False
                        break
            else:
                for k in range(1, 10):
                    for digit in change:
                        list_nb = list(nb)
                        list_nb[digit] = str(k)
                        nb = ''.join(list_nb)
                    res.append(nb)
                    if not isPrime(int(nb)):
                        count += 1
                    if count == 2:
                        flag = False
                        break
            if flag:
                return res
            else:
                pass
    return []
                
def solve():
    n = 56000
    while(1):
        # print n
        res = verify(str(n))
        if len(res) >= 8:
            return res[0]
        else:
            n += 1

if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)