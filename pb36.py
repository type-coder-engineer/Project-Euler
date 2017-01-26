#coding: utf
import time

def isPalindromic(string):
    for index in range(int(len(string) / 2)):
        if string[index] == string[-index - 1]:
            continue
        else:
            return False
    return True
    
def solve():
    res = 0
    for index in range(1, 1000001):
        if isPalindromic(str(index)) and isPalindromic(bin(index)[2:]): # 注意用bin转换后的string一开始有一个'0b'项要去掉
            res += index
        else:
            pass
    return res
    
if __name__ == '__main__':
    start = time.time()
    # print isPalindromic(bin(585))
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)