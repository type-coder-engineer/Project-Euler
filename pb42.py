#coding: utf
import time

def readFile(filename):
    list_word = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        for word in line.split(','):
            list_word.append(eval(word)) # 用eval() 来去除原本的"" ""
    # print list_word
    return list_word

def listNb():
    n = 2
    list_nb = [1]
    while(list_nb[-1] < 1000):
        list_nb.append(0.5 * n * (n + 1))
        n += 1
    return list_nb

def solve(list_word, list_nb):
    count = 0
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for word in list_word:
        value = 0
        for letter in word:
            value += alphabet.index(letter) + 1
        if value in list_nb:
            count += 1
        else:
            pass
    return count
    
if __name__ == '__main__':
    start = time.time()
    list_word = readFile('input_42.txt')
    list_nb = listNb()
    print "The answer is {}".format(solve(list_word, list_nb))
    end = time.time()
    print "it took {} seconds".format(end - start)