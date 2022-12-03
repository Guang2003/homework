fucking_input = input()
fucking_lower_input = fucking_input.lower()
testlist = []
for i in fucking_lower_input:
    if ord(i)>=65 or ord(i)==32:
        testlist.append(i)
not_fucking_anymore = ''.join(testlist)
should_be_work_fuck = []
should_be_work_fuck = not_fucking_anymore.split()

dic = {}
for i in should_be_work_fuck:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
#print(len(dic))
b = 0
c = 0
d = len(dic)
while b < d:
    a = int(0)
    for i in dic:
        if a < dic[i]:
            a = dic[i]
            c = i
    print(c,dic[c])
    dic.pop(c)
    b += 1
    #print(dic)