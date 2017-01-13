#coding: utf
import time
import copy

def read_file(filename):
    list_nb = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        row = []
        for one in line.split(' '):
            row.append(int(one))
        list_nb.append(row)
    return list_nb    

def solve(list):
    max = 0
    list_copy = copy.copy(list)
    list_copy[1][0] += list_copy[0][0]
    list_copy[1][1] += list_copy[0][0]
    
    for i in range(2, len(list_copy)):
        list_copy[i][0] += list_copy[i - 1][0]
        list_copy[i][-1] += list_copy[i - 1][-1]
        for j in range(1, len(list_copy[i]) - 1):
            list_copy[i][j] += is_larger(list_copy[i - 1][j], list_copy[i - 1][j - 1])
    # print list_copy
    for one in list_copy[-1]:
        max = is_larger(one, max)
    return max
    
def is_larger(a, b):
    return a if a > b else b
    
if __name__ == '__main__':
    start = time.time()
    list_nb = read_file('input_18.txt')
    print "The answer is {}".format(solve(list_nb))
    end = time.time()
    print "it took {} seconds".format(end - start)