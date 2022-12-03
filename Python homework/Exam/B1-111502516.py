"""
Bonus 01
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""
file = open('num.txt','r')
tgt = file.read().split()
file.close()
files = open('invoice.txt','r')
demo = files.read().split()
files.close()
special = 0
not_special = 0
count_tgt = -1
count = 0
demolen = len(demo)
special_tgt = tgt[0]
not_special_tgt = tgt[1]
top_tgt1 = tgt[2]
top_tgt2 = tgt[3]
top_tgt3 = tgt[4]
small_tgt1 = tgt[5]
small_tgt2 = tgt[6]
small_tgt3 = tgt[7]

for i in demo:
    if i == special_tgt:
        special += 1
    if i == not_special_tgt:
        not_special += 1

def top_price():
    global top
    top = 0
    global second
    second = 0
    global third
    third = 0
    global _4th
    _4th = 0
    global _5th
    _5th = 0
    global top_6th
    top_6th = 0

    for i in demo:
        count_tgt = -1
        count = 0
        for j in i[::-1]:
            #print(j)
            if j == top_tgt1[count_tgt]:
                count += 1
                count_tgt -= 1
                continue
            break
        if count == 8:
            top += 1
        if count == 7:
            second += 1
        if count == 6:
            third += 1
        if count == 5:
            _4th += 1
        if count == 4:
            _5th += 1
        if count == 3:
            top_6th += 1

    for i in demo:
        count_tgt = -1
        count = 0
        for j in i[::-1]:
            #print(j)
            if j == top_tgt2[count_tgt]:
                count += 1
                count_tgt -= 1
                continue
            break
        if count == 8:
            top += 1
        if count == 7:
            second += 1
        if count == 6:
            third += 1
        if count == 5:
            _4th += 1
        if count == 4:
            _5th += 1
        if count == 3:
            top_6th += 1

    for i in demo:
        count_tgt = -1
        count = 0
        for j in i[::-1]:
            #print(j)
            if j == top_tgt3[count_tgt]:
                count += 1
                count_tgt -= 1
                continue
            break
        if count == 8:
            top += 1
        if count == 7:
            second += 1
        if count == 6:
            third += 1
        if count == 5:
            _4th += 1
        if count == 4:
            _5th += 1
        if count == 3:
            top_6th += 1

def extra_small_price():
    global small_6th
    small_6th = 0
    for i in demo:
        count_tgt = -1
        count = 0
        for j in i[-1:-4:-1]:
            if j == small_tgt1[count_tgt]:
                count += 1
                count_tgt -= 1
                
                continue
            break
        if count == 3:
            small_6th += 1
            
    for i in demo:
        count_tgt = -1
        count = 0
        for j in i[-1:-4:-1]:
            if j == small_tgt2[count_tgt]:
                count += 1
                count_tgt -= 1
                continue
            break
        if count == 3:
            small_6th += 1
            
    for i in demo:
        count_tgt = -1
        count = 0
        for j in i[-1:-4:-1]:
            if j == small_tgt3[count_tgt]:
                count += 1
                count_tgt -= 1
                continue
            break
        if count == 3:
            small_6th += 1



top_price()
extra_small_price()
no_price_num = demolen-(special+not_special+top+second+third+_4th+_5th+top_6th+small_6th)
total_list = [special,not_special,top,second,third,_4th,_5th,top_6th+small_6th,no_price_num]
total_price = special*10000000+not_special*2000000+top*200000+second*40000+third*10000+_4th*4000+_5th*1000+top_6th*200+small_6th*200

def Output( count, total ) :
    # count為一個list，包含特別獎、特獎、頭獎、二獎、三獎、四獎、五獎、六獎和沒中獎的次數
    # total為中獎總金額
    print('特別獎：', count[0])
    print('特獎：', count[1])
    print('頭獎：', count[2])
    print('二獎：', count[3])
    print('三獎：', count[4])
    print('四獎：', count[5])
    print('五獎：', count[6])
    print('六獎：', count[7])
    print('沒中獎：', count[8])
    print(total)
Output(total_list,total_price)