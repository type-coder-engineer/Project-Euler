#coding: utf
import time

def read_file(filename):
    list_game = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        index = 0
        game = []
        for card in line.split(' '):
            game.append(card)
        list_game.append(game)
    return list_game

def ranking(poker):
    list_nb = []
    list_color = []
    order = '23456789TJQKA'
    for index in range(len(poker)):
        list_nb.append(poker[index][0])
        list_color.append(poker[index][1])
    dic_card = nbOfCard(list_nb)
    length = len(dic_card)
    list_nb = list(set(list_nb))
    
    if length != 5:
        list_order = []
        if length == 4:
            for key, value in dic_card.items():
                if value == 2:
                    list_order.append(order.index(key))
                    list_nb.remove(key)
                    break
            myOrder = getOrder(list_nb)
            for i in range(len(myOrder)):
                list_order.append(order.index(myOrder[-i - 1]))
            return (8, list_order)
            
        elif length == 3:
            if 3 in dic_card.values():
                for key, value in dic_card.items():
                    if value == 3:
                        list_order.append(order.index(key))
                        list_nb.remove(key)
                        break
                myOrder = getOrder(list_nb)
                for i in range(len(myOrder)):
                    list_order.append(order.index(myOrder[-i - 1]))
                return (6, list_order)
                
            else:
                for key, value in dic_card.items():
                    if value == 2:
                        list_order.append(order.index(key))
                        list_nb.remove(key)
                if list_order[0] < list_order[1]:
                    list_order[0], list_order[1] = list_order[1], list_order[0]
                myOrder = getOrder(list_nb)
                for i in range(len(myOrder)):
                    list_order.append(order.index(myOrder[-i - 1]))
                return (7, list_order)
                
        else:
            if 4 in dic_card.values():
                for key, value in dic_card.items():
                    if value == 4:
                        list_order.append(order.index(key))
                        list_nb.remove(key)
                        break
                list_order.append(order.index(list_nb[0]))
                return (2, list_order)
                
            else:
                for key, value in dic_card.items():
                    if value == 3:
                        list_order.append(order.index(key))
                        list_nb.remove(key)
                        break
                list_order.append(order.index(list_nb[0]))
                return (3, list_order)
            
    else:    
        myOrder = getOrder(list_nb)
        if myOrder in order:
            if len(set(list_color)) == 1:
                return (1, order.index(myOrder[-1]))
            else:
                return (5, order.index(myOrder[-1]))
        else:
            if len(set(list_color)) == 1:
                return (4, 0)
            else:
                return (9, [order.index(myOrder[-1]), order.index(myOrder[-2]), order.index(myOrder[-3]), order.index(myOrder[-4]), order.index(myOrder[-5])])

def getOrder(list_nb):
    order = '23456789TJQKA'
    myOrder = ''
    dic_order = {}
    for hand in list_nb:
        dic_order[order.index(hand)] = hand
    trueOrder = dic_order.keys()[:]
    trueOrder.sort()
    for key in trueOrder:
        myOrder += dic_order[key]
    return myOrder
    
def nbOfCard(cards):
    dic_nb = {}
    uniqueCards = list(set(cards))
    for card in uniqueCards:
        nb = 0
        for one in cards:
            if card == one:
                nb += 1
        dic_nb[card] = nb
    return dic_nb   
            
def compare(player1, player2):
    rank1 = ranking(player1)
    rank2 = ranking(player2)
    if rank1[0] < rank2[0]:
        return 1
    elif rank1[0] > rank2[0]:
        return 2
    else:
        if rank1[0] == 4:
            return 0
        else:
            for index in range(len(rank1[1])):
                if rank1[1][index] == rank2[1][index]:
                    pass
                elif rank1[1][index] > rank2[1][index]:
                    return 1
                else:
                    return 2
            return 0

def solve(list_game):
    res = 0
    for game in list_game:
        if compare(game[0:5], game[5:]) == 1:
            res += 1
    return res
    
if __name__ == '__main__':
    start = time.time()
    # print ranking(['2K', '3K', '4K', '5K', 'AK'])
    list_game = read_file('input54_poker.txt')
    # print list_game
    print "The answer is {}".format(solve(list_game))
    end = time.time()
    print "it took {} seconds".format(end - start)