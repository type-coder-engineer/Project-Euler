#coding: utf
import time
 
# 因为最大的数是987654321，而n最小是2，所以遍历到987654321 / 3 = 329218107 即可 
def solve():
    max = 0
    for nb in range(9, 329218107):
        res = verify(nb)
        # if res != 0:
            # print res
        max = res if res > max else max
    return max
    
def verifyPandigital9(string):
    if '0' in string:
        return False
    else:
        for i in range(1, 9):
            if string[i] in string[:i]:
                return False
            else:
                pass
    return True
    
def verify(nb):
    string = ''
    for i in range(1, 10):
        string += str(nb * i)
        if len(string) == 9:
            if verifyPandigital9(string):
                return int(string)
            else:
                return 0
        elif len(string) > 9:
            return 0
        else:
            pass
            
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)