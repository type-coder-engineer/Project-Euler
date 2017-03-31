#coding: utf
import time

# 用于解决数独题目时判断每个空格不能填入的数字    
def limit_solve(map, row, col):
    list_limit = []
    
    #先将row和col中已经有的数字加入list, 这里是两边的数字
    for one in xrange(9):
        if map[row*9 + one] != 0:
            list_limit.append(map[row*9 + one])
    for one in xrange(9):
        if map[one*9 + col] != 0:
            list_limit.append(map[one*9 + col])
        
    # 再找出小的3*3的矩阵中出现的数字，这里是所有9个数字都要遍历
    local_row = (row // 3) * 3
    local_col = (col // 3) * 3
    for i in xrange(local_row, local_row + 3):
        for j in xrange(local_col, local_col + 3):
            if map[9*i + j] != 0:
                list_limit.append(map[9*i + j])
        
    return list(set(list_limit))
    
def sudoku_solving(puzzle):
    map_solved = []
    pos_blank = []
    stack_options = []
    all = range(1, 10)
    for index in xrange(81):
        if puzzle[index] == 0:
            pos_blank.append(index)
    blank_nb = len(pos_blank)
    index = 0
    origin = puzzle[:]
    flag_over = False
    
    while(1):
        row = pos_blank[index] // 9
        col = pos_blank[index] % 9
        already = limit_solve(puzzle, row, col)
        options = [one for one in all if one not in already]
        
        # 如果除去不能填的数字还可以选择那么就填入任意一个选择，然后把剩余的选择放入stack中
        if len(options) > 0:
            puzzle[pos_blank[index]] = options.pop(0)
            stack_options.append(options)
            index += 1
            if index == blank_nb:
                map_solved.append(puzzle[:])
                index = 0
                first_option = []
                for one in stack_options:
                    if len(one) == 0:
                        index += 1
                    else:
                        first_option = one[:]
                        break
                if not first_option:
                    break
                puzzle[pos_blank[index] + 1:] = origin[pos_blank[index] + 1:]
                puzzle[pos_blank[index]] = first_option.pop(0)
                stack_options = [first_option]
                index += 1
                continue
        else:
        # 如果没有可以填的选择，那么将上一个数字换成另一个选择
            last_options = []
            while(len(last_options) == 0):
                if not stack_options: # 说明已经用尽了可能了
                    flag_over = True
                    break
                last_options = stack_options.pop()
                index -= 1
                puzzle[pos_blank[index]] = 0 # 注意这里和生成数独终盘的时候不一样，如果这个要
                # 往前回溯的话必须要将已经填入的数字清零
            if flag_over:
                break
            puzzle[pos_blank[index]] = last_options.pop(0)
            stack_options.append(last_options)
            index += 1
    if len(map_solved) == 1:
        string = ''
        string += str(map_solved[0][0])
        string += str(map_solved[0][1])
        string += str(map_solved[0][2])
        return int(string)
    elif len(map_solved) > 1:
        for index in xrange(len(map_solved)):
            print_map(map_solved[index])
            print '***************'
        print 'Not unique solution, this puzzle is not a good sudoku'
    else:
        print 'No solution for this puzzle...'
    return
    
def get_puzzle():
    puzzleAll = []
    puzzleOne = []
    target = open('input96_sudoku.txt')
    index = 0
    for line in target:
        if (index % 10 == 0):
            if len(puzzleOne) == 0:
                pass
            else:
                puzzleAll.append(puzzleOne)
                puzzleOne = []
        else:
            line = line.strip('\n')
            for one in line:
                puzzleOne.append(int(one))
        index += 1
    puzzleAll.append(puzzleOne)
    return puzzleAll
    
if __name__ == '__main__':
    start = time.time()
    listPuzzle = get_puzzle()
    sum = 0
    for one in listPuzzle:
        sum += sudoku_solving(one)
    print sum
    end = time.time()
    print "it took {} seconds".format(end - start)
    
    
    