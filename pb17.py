#coding: utf
import time

def solve():
    total_nb = 0
    nb_1_dic = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    nb_10_dic = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nighteen'}
    nb_20_dic = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    
    for index in range(1, 1001):
        if index == 1000:
            total_nb += (len('one') + len('thousand'))
            continue
            
        a = index // 100
        if a != 0:
            total_nb += (len(nb_1_dic[a]) + len('hundred'))
            index -= 100 * a
            if index != 0:
                total_nb += len('and')
        else:
            pass
        # print total_nb
        
        a = index // 10
        if a != 0:
            if a == 1:
                total_nb += len(nb_10_dic[index])
                continue
            else:
                total_nb += len(nb_20_dic[a])
                index -= 10 * a
        else:
            pass
        # print total_nb
        
        if index != 0:
            total_nb += len(nb_1_dic[index])
        else:
            pass
            
    return total_nb
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)