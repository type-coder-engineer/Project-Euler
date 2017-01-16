#coding: utf
import time
import math

def sum_divisors(nb):
    sum = 0
    for i in range(1, nb):
        if nb % i == 0:
            sum += i
    return sum
    
def solve():
    sum_dic = {}
    amicable_list = []
    sum_amicable = 0
    for index in range(2, 10000):
        sum_dic[index] = sum_divisors(index)
    # print sum_dic
    # raw_input()
    for first_nb in range(2, 10000):
        for key, value in sum_dic.items():
            if value == first_nb and key == sum_dic[first_nb] and value != key:
                amicable_list.append(str(first_nb) + ': ' + str(sum_dic[first_nb]))
                sum_amicable += key # 每次只能加上key而不能也算上value，不然就会重复了
            else: 
                pass
    print amicable_list
    return sum_amicable
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)