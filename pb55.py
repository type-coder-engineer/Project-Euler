#coding: utf
import time

def palindrome(nb):
	string = str(nb)
	length = len(string)
	for index in range(length/2):
		if string[index] == string[-index - 1]:
			pass
		else:
			return False
	return True
	
def reverse(nb):
    string = str(nb)
    length = len(string)
    new_string = ''
    for i in range(length):
        new_string += string[-i - 1]
    return int(new_string)

def ifLychrel(nb):
    counting = 0
    while (counting <= 50):
        nb += reverse(nb)
        counting += 1
        if palindrome(nb):
            return False
        else:
            pass
    return True

def solve():
    res = 0
    for nb in range(10, 10000):
        if ifLychrel(nb):
            print nb
            res += 1
        else:
            pass
    return res
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    # print ifLychrel(349)
    end = time.time()
    print "it took {} seconds".format(end - start)
		


