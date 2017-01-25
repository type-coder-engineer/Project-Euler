#coding: utf
import time
import math

# 因为facotrial(9) * n < 10 ** n 中n最小整数是7，所以要一直验证到9999999
# 有一个有意思的地方，第一次运行的时候算了99秒，然后第二次和第三次10秒内就得到结果了
def solve():
    res = 0
    for index in range(11, 9999999):
        if sum(math.factorial(int(one)) for one in str(index)) == index:
            print index
            res += index
    return res
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)