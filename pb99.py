#coding: utf
import time
import math

def solve(data):
    index = 1
    index_max = 1
    max = 0
    for one in data:  
        base = math.log(int(one[0]))
        cal = base * int(one[1])
        if cal > max:
            max = cal
            index_max = index
        index += 1
    return index_max
    
# def power(a, b):
    # power_list = two_split(b)
    # res = 1
    # for i in range(power_list[0]):
        # if (i in power_list):
            # res *= a
        # a = a**2
    # res *= a
    # return res
    
# def two_split(b):
    # res = []
    # index = 0
    # while (b > 0):
        # if (b - 2**index >= 0):
            # index += 1
        # else:
            # b = b - 2**(index - 1)
            # res.append(index - 1)
            # index = 0
    # return res
    
# def two_split(b):
    # res = []
    # index = 0
    # while(b > 0):
        # if (b&1 == 1):
            # res.append(index)
        # else:
            # pass
        # index += 1
        # b = (b>>1)
    # return res
    
def read_file(filename):
    data = []
    target = open(filename)
    for line in target:
        line = line.strip('\n')
        a, b = line.split(',')
        data.append((int(a), int(b)))
    return data
    
if __name__ == '__main__':
    start = time.time()
    # print two_split(99999)
    data = read_file('input_99.txt')
    print "The answer is {}".format(solve(data))
    end = time.time()
    print "it took {} seconds".format(end - start)
