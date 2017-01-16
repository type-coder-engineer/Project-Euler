#coding: utf
import time

def read_file(filename):
    list_name = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        for name in line.split(','):
            list_name.append(eval(name))
    return list_name

def worth_word(word):
    worth = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    for letter in word:
        worth += alphabet.index(letter) + 1
    return worth
   
def solve(list_name):
    sum = 0
    list_name.sort()
    for index in range(0, len(list_name)):
        sum += (index + 1) * worth_word(list_name[index])
    return sum
    
if __name__ == '__main__':
    start = time.time()
    list_name = read_file('input_22.txt')
    print "The answer is {}".format(solve(list_name))
    end = time.time()
    print "it took {} seconds".format(end - start)