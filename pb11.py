#coding: utf
import time

def read_file(filename):
    list_nb = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        new_row = []
        for nb in line.split(' '):
            # print nb
            # raw_input()
            if nb[0] == '0':
                new_row.append(int(nb[1]))
            else:
                new_row.append(int(nb))
        list_nb.append(new_row)
    return list_nb

def direction4_sum(position, list):
    max = 1
    if position[0] >= 3:
        for i in range(0, 4):
            max *= list[position[0] - i][position[1]]
            
    if position[0] <= len(list) - 4:
        sum = 1
        for i in range(0, 4):
            sum *= list[position[0] + i][position[1]]
        if sum > max:
            max = sum
        else:
            pass
            
    if position[1] >= 3:
        sum = 1
        for i in range(0, 4):
            sum *= list[position[0]][position[1] - i]
        if sum > max:
            max = sum
        else:
            pass
            
    if position[1] <= len(list[0]) - 4:
        sum = 1
        for i in range(0, 4):
            sum *= list[position[0]][position[1] + i]
        if sum > max:
            max = sum
        else:
            pass

    return max
    
def diagonal_sum(position, list):
    max = 1
    if position[0] >= 3 and position[1] >= 3:
        for i in range(0, 4):
            max *= list[position[0] - i][position[1] - i]
            
    if position[0] <= len(list) - 4 and position[1] >= 3:
        sum = 1
        for i in range(0, 4):
            sum *= list[position[0] + i][position[1] - i]
        if sum > max:
            max = sum
        else:
            pass
            
    if position[1] <= len(list[0]) - 4 and position[0] >= 3:
        sum = 1
        for i in range(0, 4):
            sum *= list[position[0] - i][position[1] + i]
        if sum > max:
            max = sum
        else:
            pass
            
    if position[1] <= len(list[0]) - 4 and position[0] <= len(list) - 4:
        sum = 1
        for i in range(0, 4):
            sum *= list[position[0] + i][position[1] + i]
        if sum > max:
            max = sum
        else:
            pass
        
    return max

def bigger(a, b):
    return a if a > b else b
    
def solve(list):
    max = 1
    for i in range(0, len(list)):
        for j in range(0, len(list[0])):
            pos = (i, j)
            sum = bigger(direction4_sum(pos, list), diagonal_sum(pos, list))
            if sum > max:
                max = sum
            else:
                pass
    return max
           
if __name__ == '__main__':
    start = time.time()
    list = read_file('input_11.txt')
    # print list
    print 'the answer is {}'.format(solve(list)) 
    end = time.time()
    print 'it took {} seconds'.format(end - start)