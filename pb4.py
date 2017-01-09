#coding: utf
import math
import time

def is_palindromic(string):
    length = len(string)
    for index in range(0, length/2):
        if string[index] == string[-(index + 1)]:
            pass
        else:
            return False
    return True

def solve():
    time1 = 999
    time2 = 999
    max = 0
    while(time1 >= 100 and time2 >= 100):  # 注意这里一定是>=，不然time2减到100的时候就跳出循环了
        res = time1 * time2
        if is_palindromic(str(res)):
            if res > max:
                max = res
        else:
            pass
        if time2 > 100:
            time2 -= 1
        else:
            time1 -= 1
            time2 = 999
    
    if max:
        return max
    else:
        return 'no answer...'  
    
if __name__ == '__main__':
    start = time.time()
    print 'the answer is {}'.format(solve()) 
    end = time.time()
    print 'it took {} seconds'.format(end - start)
    # pypy用了0,047秒，python用了0.78秒，而swift用了2.5秒。。。