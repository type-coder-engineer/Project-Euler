# coding: utf
import time

def solve():
    max_cycle = 0
    res = 1
    for nb in range(2, 1000):
        # print  nb
        length = get_cycle(nb)
        if length > max_cycle:
            max_cycle = length
            res = nb
    return res
    
def get_cycle(nb):
    quotient_remainder = {}
    length = 0
    remainder = 1
    while(1):
        if remainder // nb == 0:
            remainder *= 10
            length += 1
            continue
        else:
            new_quotient = remainder // nb
            new_remainder = remainder % nb
            if new_remainder == 0:
                return length
            else:
                for key, value in quotient_remainder.items():
                    if value[0] == new_quotient and value[1] == new_remainder:
                        return (length - key)
                quotient_remainder[length] = (new_quotient, new_remainder) # 注意这里要用length作为key!!因为key只能有一个，用商来做的话最多只有1到9个，之后重复的会替换掉之前的情况
            remainder = new_remainder
            
        if length == 1000:
            print 'something wrong with {}'.format(nb)
            return 
  
def countRec(n):
    resti = []
    resto = 1    
    while resto:
            resto = resto % n
            if resto in resti:
                return len(resti) - resti.index(resto)
            resti.append(resto)
            print resti
            raw_input()
            resto *= 10
    return len(resti) - 1
    # 这个题目确实只要用余数来确认就可以了，不知道怎么就想要余数加商来确认的。。。
    # 这个结构也不错，如果被整除了resto就是1，直接跳出循环了，然后用顺序容器中的index方法得到长度
    
if __name__ == '__main__':
    start = time.time()
    # print get_cycle(6)
    # print countRec(23)
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)