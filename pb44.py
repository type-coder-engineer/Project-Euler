#coding: utf
import time

# def solve_old():
    # D = 10000
    # listPen = []
    # for new in pentagonal():
        # listPen.append(new)
        # if len(listPen) > 1:
            # for index in xrange(len(listPen) - 2, -1, -1):
                # diff = new - listPen[index]
                # if index == len(listPen) - 2 and diff > D:
                    # print diff
                    # print len(listPen)
                    # return D
                # else:
                    # if diff in listPen and verify(new + listPen[index]):
                        # D = diff if diff < D else D
                        # break
                    # else:
                        # pass
    # return
    
# def pentagonal():
    # n = 1
    # while(1):
        # yield n * (3 * n - 1) / 2
        # n += 1
    # return
def solve():
    n = 2
    while(1):
        # print n
        # if 3*n + 1 > D:
            # return D # 应该有这个判断条件，但是这样花的时间就太长了
        for m in range(n - 1, 0, -1):
            if verify((3*m*m + 3*n*n - m - n)/2) and verify((n - m)*(3*m + 3*n - 1)/2):
                diff = (n - m)*(3*m + 3*n - 1)/2
                return diff
            else:
                pass
        n += 1
        
def verify(nb):
    n = 1
    while(1):
        if n * (3 * n - 1) / 2 == nb:
            return True
        elif n * (3 * n - 1) / 2 > nb:
            return False
        else:
            n += 1
            
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)