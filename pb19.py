#coding: utf
import time
import copy

def solve():
    target_days = 0
    day_index = 3 # 注意问的是1901年开始，所以要算一下1月1号是星期几
    year_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for year in range(1901, 2001):
        if year % 4 == 0:
            for month in year_leap:
                day_index = (day_index + month) % 7
                # print day_index
                # raw_input()
                if day_index == 0:
                    target_days += 1
        else:
            for month in year_normal:
                day_index = (day_index + month) % 7
                # print day_index
                # raw_input()
                if day_index == 0:
                    target_days += 1
    return target_days
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)