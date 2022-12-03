#count = 0
top = 0
second = 0
third = 0
_4th = 0
_5th = 0
_6th = 0
tgt = []
num = []
while True:
    item = input()
    if item == '.':
        break
    else:
        tgt.append(item)
while True:
    items = input()
    if items == '.':
        break
    else:
        num.append(items)
#print(tgt,num)
count_tgt = -1
for i in tgt:
    
    for j in num:
        #print(j)
        count = 0
        count_tgt = -1
        for k in j[::-1]:
            if k == i[count_tgt]:
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
            _6th += 1
print(top*200000+second*40000+third*10000+_4th*4000+_5th*1000+_6th*200)