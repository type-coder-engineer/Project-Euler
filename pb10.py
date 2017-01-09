#coding: utf
import math

def get_primes():
    nb = 3
    while True:
        if is_prime(nb):
            yield nb
        nb += 1    
        
def is_prime(nb):
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
    
def solve_pb():
    total = 2
    for next in get_primes():
        # print next
        if next <= 2000000:
            total += next
        else:
            return total     
            
if __name__ == '__main__':
    print solve_pb()

