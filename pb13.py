#coding: utf
import math
import time

def read_file(filename):
    list_nb = []
    index = 0
    for line in open(filename, 'r'):
        line = line.strip('\n')
        list_nb.append(line)
    return list_nb
    
def solve(list_nb):
    sum = 0
    for one in list_nb:
        sum += int(one)
    string = str(sum)
    return string[0:10]
    
if __name__ == '__main__':
    start = time.time()
    list_nb = read_file('input_13.txt')
    # print list_nb
    # print len(list_nb)
    print 'the answer is {}'.format(solve(list_nb)) 
    end = time.time()
    print 'it took {} seconds'.format(end - start)