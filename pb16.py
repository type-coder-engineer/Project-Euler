#coding: utf
import time

def solve():
    # sum = 0
    # for one in str(2 ** 1000):
        # sum += int(one)
    # return sum
    return sum(int(one) for one in str(2 ** 1000))
    # 简洁优雅！！
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)