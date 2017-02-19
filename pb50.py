#coding: utf
import time, math

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

def prime_generator(start_index):
    n = 2
    index = 1
    while(1):
        while(index < start_index):
            if isPrime(n):
                index += 1
            n += 1
        if isPrime(n):
            yield n
        n += 1
    return 
    
def solve():
    longest = 0
    res = 0
    start = 0
    while(1):
        start += 1
        sum = 0
        pre = 0
        index = 0
        nb = 0
        end_prime = 0
        for prime in prime_generator(start):
            sum += prime
            index += 1
            if sum >= 1000000:
                if nb > longest:
                    longest = nb
                    res = pre
                    if end_prime > (1000000 - pre):
                        return res
                    else:
                        pass
                break
            if isPrime(sum):
                pre = sum
                nb = index
                end_prime = prime
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)