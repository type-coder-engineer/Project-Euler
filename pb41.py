#coding: utf
import time
import math

def isPrime(nb):
    if nb > 1:
        if nb == 2:
            return True
        elif nb % 2 == 0:
            return False
        for possible in xrange(3, int(math.sqrt(nb) + 1), 2): # 注意xrange是generator，而range是生成一个list，所以只是迭代的话使用xrange
            if nb % possible == 0:
                return False
        return True
    return False

def isPandigital(string):
    if '0' in string:
        return False
    else:
        for i in xrange(len(string)):
            if string[i] in string[:i]:
                return False
            else:
                pass
        string_nb = '123456789'
        for one in string_nb[0:len(string)]:
            if one not in string:
                return False
            else:
                pass
    return True
    
def solve():
    # 因为9位和8位的pandigital都肯定能被3整除，所以直接从7位最大的7654321开始尝试
    for index in xrange(7654321, 2, -2):
        # print index
        if isPandigital(str(index)) and isPrime(index): # 注意两个条件的话把计算量小的放在前面能节省好多倍的时间
            return index
        else:
            pass 
     
if __name__ == '__main__':
    start = time.time()
    # print isPandigital('654321')
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)