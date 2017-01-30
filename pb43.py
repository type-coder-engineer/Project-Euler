#coding: utf
import time
import itertools

def solve():
    sum = 0
    for num in itertools.permutations(range(10)):
        if num[0] == 0:
            continue
        else:
            string = ''
            for one in num:
                string += str(one)
            if verify(string):
                # print string
                sum += int(string)
            else:
                pass
    return sum

def verify(string):
    listPrime = (2,3,5,7,11,13,17)
    for i in range(0, 7):
        if int(string[i + 1 : i + 4]) % listPrime[i] == 0:
            pass
        else:
            return False
    return True

if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)