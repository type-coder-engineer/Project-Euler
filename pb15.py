#coding: utf
import time

# bfs算法的典型应用，不重复的最多路径
# 但是这道题不适合，数值太大，不能暴力枚举
def bfs_all_path(row, column):
    nb_path = 0
    stack = [(0,0)]
    
    while(stack):
        print len(stack)
        pos = stack.pop(0)
        if pos  == (row, column):
            nb_path += 1
            continue
        else:
            pass
        
        x, y = pos
        if x < row:
            stack.append((x + 1, y))
        if y < column:
            stack.append((x, y + 1))
            
    return nb_path

    # 使用顶点和算法，花费0秒
def solve():
    row = 20
    column = 20
    map = [[0 for row in range(row + 1)] for column in range(column + 1)]
    for i in  range(1, row + 1):
        map[i][0] = 1
        map[0][i] = 1
    
    for index in range(2, 2 * row + 1):
        for i in range(1, row + 1):
            for j in range(1, column + 1):
                if i + j == index: # 这样来达到对脚线推进的效果
                    map[i][j] = map[i - 1][j] + map[i][j - 1]
                    
    return map[row][column]
    
if __name__ == '__main__':
    start = time.time()
    # print "The answer is {}".format(bfs_all_path(20, 20))
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)