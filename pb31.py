#coding: utf
import time

# 使用递归只用了1.5s
def solve():
    global ways
    ways = 0
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    value = 1 # 表示最高的节点从coins中的200开始
    all_the_ways(coins, target, 0, value)
    return ways
    
def all_the_ways(coins, target, sum, value):
    global ways
    for i in range(target / coins[-value] + 1):
        if sum + i * coins[-value] == target:
            ways += 1
            return 
        else:
            if value == len(coins):
                pass
            else:
                all_the_ways(coins, target, sum + i * coins[-value], value + 1)  # 因为已有价值sum的传递
                #是给下一个节点的，病假不能影响这个节点别的支路，所以就在形参中传递值的变化                

    # bad way... I feel embarrassed to write these codes
# def solve():
    # coins = [1, 2, 5, 10, 20, 50, 100, 200]
    # target = 200
    # ways = 0
    # for value1 in range(0, target + coins[0], coins[0]):
        # for value2 in range(0, target + coins[1], coins[1]):
            # for value3 in range(0, target + coins[2], coins[2]):
                # for value4 in range(0, target + coins[3], coins[3]):
                    # for value5 in range(0, target + coins[4], coins[4]):
                        # for value6 in range(0, target + coins[5], coins[5]):
                            # for value7 in range(0, target + coins[6], coins[6]):
                                # for value8 in range(0, target + coins[7], coins[7]):
                                    # if value1 + value2 + value3 + value4 + value5 + value6 + value7 + value8 == target:
                                        # ways += 1
                                    # else:
                                        # pass
    # return ways
    
if __name__ == '__main__':
    start = time.time()
    print "The answer is {}".format(solve())
    end = time.time()
    print "it took {} seconds".format(end - start)