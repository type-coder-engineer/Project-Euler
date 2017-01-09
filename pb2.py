#coding: utf

def fibonacci(max):
    a = 1
    f = 1
    while(f <= max):
        yield f
        b = a
        a = f
        f = f + b
    return
        
def is_even(nb):
    return True if nb % 2 == 0 else False
    
def sum():
    total = 0
    for nb in fibonacci(4000000):
        if is_even(nb):
            # print nb
            # raw_input()
            total += nb
    return total

if __name__ == '__main__':
    print sum()