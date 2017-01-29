#coding: utf
import time

def solve():
    res = 1
    index = [10, 100, 1000, 10000, 100000, 1000000]
    for one in index:
        res *= det(one)
    return res
    
def det(index):
    index -= 9
    circle_nb = 1 
    while(1):
        # print circle_nb
        myUnit = unit(circle_nb)
        index -= 10 * (myUnit + 1)
        if index <= 0:
            return find_nb(index + 10 * (myUnit + 1), circle_nb, myUnit)
        else:
            circle_nb += 1
        
def unit(nb):
    i = 1
    while(1):
        if nb - 10 ** i < 0:
            return i
        else:
            i += 1

def find_nb(index, circle_nb, unit):
    count = index // (unit + 1) - 1
    rest = index % (unit + 1)
    if rest == 0:
        return count
    else:
        return int(str(circle_nb)[rest - 1])
            
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)