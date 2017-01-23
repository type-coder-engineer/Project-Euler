#coding: utf
import time
import math

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
    
def solve():
    index_max = 0
    # product = []
    product = 0
    for a in range(-999, 1000):
        # print a
        # raw_input()
        for b in range(-1000, 1001):
            if not is_prime(b):
                continue
            else:
                pass
            n = 0
            index = 0
            while(1):
                if is_prime(n**2 + a * n + b):
                    index += 1
                    n += 1
                else:
                    break
            if index > index_max:
                # product[:] = []
                # product.append(a * b)
                # product.append(a)
                # product.append(b)
                # product.append(index)
                product = a * b 
                index_max = index # 怎么把这个忘了。。。简直醉了
            else:
                pass
    return product
                
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)