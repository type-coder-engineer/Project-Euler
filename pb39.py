#coding: utf
import time
 
def solve():
    max = 0
    max_p = 0
    for p in range(12, 1001):
        res = nbRightTriangle(p)
        if res > max:
            max_p = p
            max = res
    return max_p
    
def nbRightTriangle(p):
    nb = 0
    for c in range(int(p / 3), int(p / 2)):
        for a in range(1, p - c):
            if a ** 2 + (p - c - a) ** 2 == c ** 2:
                nb += 1
                break # 不然的话会有a和b互换的重复
            else:
                pass
    return nb    
 
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)