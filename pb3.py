#coding: utf
import math
import time

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
    
def reverse_factor1(nb):
    index = 1
    while index < nb:
        # print index
        if nb % index == 0:
            # print (nb / index)
            # print '**********'
            yield nb / index
        else:
            pass
        index += 1
    return
    
def reverse_factor2(nb):
    index = nb
    while index > 1:
        # print index
        if nb % index == 0:
            # print (nb / index)
            # print '**********'
            yield index
        else:
            pass
        index -= 1
    return
    
def solve():
    nb = 600851475143
    # nb = 13195
    for possible in reverse_factor2(nb):
        if is_prime(possible):
            print '************'
            return possible
        else:
            pass
            
def solve_recursion(nb):
    # print nb
    if is_prime(nb):
        return nb
    else:
        index = 2
        while(index < nb):
            if nb % index == 0:
                factor = nb/index
                res = solve_recursion(factor)
                break # 注意这个递归里面套了一个循环，所以找到一个之后要立刻break掉
            else:
                index += 1
    return res        
    
if __name__ == '__main__':
    start = time.time()
    # print 'The answer is {}'.format(solve())
    print 'The answer is {}'.format(solve_recursion(600851475143))
    # 方法一遍历的话要花3.7s，但是递归只要0s，毕竟省去了许多步骤
    end = time.time()
    print 'it took {} seconds'.format(end - start)
    # start = time.time()
    # for i in range(1, 10000000):
        # if (i + 1) % i == 0:
            # pass
    # end = time.time()
    # print 'it took {} seconds'.format(end - start)
    # start = time.time()
    # for i in range(20000000, 10000000, -1):
        # if (i + 1) % i == 0:
            # pass
    # end = time.time()
    # print 'it took {} seconds'.format(end - start)
    # 实验表明遍历的方向和速度关系不大，计算较大的数字也相差不大，所以reverse_factor2的问题还是
    # 遍历的数目过多，毕竟量级不一样。
    
    
    
    
    
    
    
    