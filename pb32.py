#coding: utf
import time
import math

def pandigital(nb):
    contents = []
    for one in str(nb):
        if one in contents:
            return False
        else:
            contents.append(one)
    return True
    
def multiplier_pandigital(nb):
    for i in range(2, int(round(math.sqrt(nb)))):
        if nb % i == 0:
            if pandigital(i) and pandigital(nb / i):
                if verify(i, nb / i, nb):
                    return [i, nb / i]
                else:
                    pass 
            else:
                pass
        else:
            pass
    return []

def verify(multi1, multi2, product):
    contents = []
    for one in str(multi1) + str(multi2) + str(product):
        if one in contents:
            return False
        else:
            contents.append(one)
    if len(set(contents)) == 9 and '0' not in contents:
        return True
    else:
        return False
    
    # 因为99*999 = 98901 一共有10位数了，所以乘积不能超过100000
def solve():
    sum = 0
    list = []
    for index in range(1, 100000):
        # print index
        if pandigital(index):
            res =  multiplier_pandigital(index)
            if len(res) != 0:
                list.append('{} = {} x {}'.format(index, res[0], res[1]))
                sum += index
            else:
                pass
        else:
            pass
    print list
    return sum

if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)