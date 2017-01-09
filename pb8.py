#coding: utf
import math
import time

def read_file(filename):
    string_nb = ""
    for line in open(filename, 'r'):
        line = line.strip('\n')
        string_nb += line
    return string_nb

def sum_13(index, string):
    sum = 1
    for i in range(0, 13):
        sum *= int(string[index + i])
    return sum
    
def solve(string_nb):
    max = 0
    for i in range(0, len(string_nb) - 12):
        sum = sum_13(i, string_nb)
        if max < sum:
            max = sum
        else:
            pass
    return max
    
if __name__ == '__main__':
    start = time.time()
    string = read_file('input_8.txt')
    print 'the answer is {}'.format(solve(string)) 
    end = time.time()
    print 'it took {} seconds'.format(end - start)