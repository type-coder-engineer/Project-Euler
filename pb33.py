#coding: utf
import time

def solve():
    res_dic = {}
    for denominator in range(11, 100):
        for numertor in range(10, denominator):
            if verify(numertor, denominator):
                res_dic[numertor] = denominator
            else:
                pass
    # print res_dic
    if len(res_dic) != 4:
        print "may have some problems"
    else:
        pass
        
    myNum = 1
    myDen = 1
    for key, value in res_dic.items():
        myNum *= key
        myDen *= value
    return simplify(myNum, myDen)[1]

def verify(numertor, denominator):
    num = str(numertor)
    den = str(denominator)
    if num[0] == den[1]:
        if den[0] != '0' and float(num[1]) / int(den[0]) == float(numertor) / denominator:
            return True
        else:
            pass
    elif num[1] == den[0]:
        if den[1] != '0' and float(num[0]) / int(den[1]) == float(numertor) / denominator:
            return True
        else:
            pass
    else:
        pass
    return False
    
def simplify(numertor, denominator):
    for common_divisor in range(2, numertor + 1):
        while (numertor % common_divisor == 0 and denominator % common_divisor == 0):
            numertor /= common_divisor
            denominator /= common_divisor
    return (numertor, denominator)    

if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)