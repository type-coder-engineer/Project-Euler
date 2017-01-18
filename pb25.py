#coding: utf
import time

def fibonacci():
    a = 0
    b = 1
    while(1):
        yield b
        c = a
        a = b
        b = c + b
    return
    
def solve():
    index = 0
    for fifi in fibonacci():
        index += 1
        if len(str(fifi)) == 1000:
            return index
    return 
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)