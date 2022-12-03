fucking_input = input()
fucking_upper_input = fucking_input.upper()
testlist = []
#print(fucking_upper_input)
for i in fucking_upper_input:
    if ord(i)>=65 or ord(i)==32:
        testlist.append(i)
#print(testlist)
not_fucking_anymore = ''.join(testlist)
#print(not_fucking_anymore)
should_be_work_fuck = []
should_be_work_fuck = not_fucking_anymore.split()

tgt = []

tgt_num = int(input())
result = []
for i in range(tgt_num):
    fucking_tgt = input()
    fucking_upper_tgt = fucking_tgt.upper()
    tgt.append(fucking_upper_tgt)


for i in tgt:
    print(should_be_work_fuck.count(i))