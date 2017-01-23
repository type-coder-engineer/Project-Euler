#coding: utf
import time

def solve():
    list_nb = []
    for a in range(2,101):
        for b in range(2,101):
            res = a**b
            if res in list_nb:
                pass
            else:
                list_nb.append(res)
    return len(list_nb)
            
if __name__ == '__main__':
	start = time.time()
	print 'The answer is {}'.format(solve())
	end = time.time()
	print "It took {} seconds".format(end - start)