#coding: utf
import time

def solve():
    Tn = 286
    Pn = 165
    Hn = 143
    while(not tri(Tn) == pen(Pn) == hex(Hn)):
        if tri(Tn) < pen(Pn) or tri(Tn) < hex(Hn):
            Tn += 1
        else:
            if pen(Pn) < tri(Tn):
                Pn += 1
            if hex(Hn) < tri(Tn):
                Hn += 1
    return tri(Tn)
            
def tri(n):
    return n*(n + 1)/2
    
def pen(n):
    return n*(3*n - 1)/2
    
def hex(n):
    return n*(2*n - 1)

if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)