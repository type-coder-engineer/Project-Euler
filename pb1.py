#coding: utf

def multiple_3(nb):
    return True if nb % 3 == 0 else False
  
def multiple_5(nb):
    return True if nb % 5 == 0 else False
    
def sum_nb():
    total = 0
    for nb in range(1, 1000):
        if multiple_3(nb) or multiple_5(nb):
            total += nb
    return total
    
if __name__ == '__main__':
    print sum_nb()