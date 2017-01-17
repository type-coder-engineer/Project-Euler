#coding: utf
import time

def get_list():
    list_abundant = []
    for index in range(1, 28124):
        if index < sum_divisors(index):
            list_abundant.append(index)
        else:
            pass
    # print list_abundant
    # raw_input()
    return list_abundant
        
def sum_divisors(nb):
    sum = 0
    for i in range(1, nb / 2 + 1):
        if nb % i == 0:
            sum += i
        else:
            pass
    return sum
    
def solve(list_abundant):
    sum = 0
    for index in range(1, 28124):
        flag_found = False
        for nb1 in list_abundant:
            if nb1 >= index or flag_found:
                break
            else:
                for nb2 in list_abundant:
                    if nb2 >= index or flag_found:
                        break
                    else:
                        if nb1 + nb2 == index:
                            flag_found = True
                        else:
                            pass
        if not flag_found:
            sum += index
            # print index
        else:
            pass
    return sum

if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve(get_list()))
    end = time.time()
    print "it took {} seconds".format(end - start)