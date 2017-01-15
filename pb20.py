#coding: utf
import time
import math

def solve():
    return sum(int(one) for one in str(math.factorial(100))) # 使用facotrial只要一行即可
    # return reduce(lambda x, y: x + y, [int(one) for one in str(reduce(lambda x, y: x*y, range(1, 101)))])
    # 也可以考虑使用build in的reduce, 连sum都不用了，不过主要是能省去factorial
    # 顺便尝试一下计算自然底数
    # return sum(float(1) / math.factorial(x) for x in range(0, 100))

if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)