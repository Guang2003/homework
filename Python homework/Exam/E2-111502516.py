"""
Exam 2
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""


def open_file():
    file = open('E2_input.txt',mode='r')
    demo_alpha = file.readline()
    demolistalpha = demo_alpha.split()
    demo_num = file.readline()
    demolistnum = demo_num.split()
    file.close()
    return demolistalpha , demolistnum
    
#print(open_file())

tgt = input()
def search_index(list1,list2, tgt):
    
    if ord(tgt)>60:
        global location
        location = 1
        for i in range(len(list1)):
            if tgt == list1[i-1]:
                return i-1
        if ord(tgt)> 118:
            return '11'
        for j in range(len(list1)):
            if ord(tgt)>ord(list1[j-1]):
                ans = j
        return ans
    else:
        location = 2
        for i in range(len(list2)):
            if tgt == list2[i]:
                return i
        if tgt > 796:
            return '11'
        for j in range(len(list2)):
            
            if int(tgt) >= int(list2[j]):
                #print(tgt,list2[j])
                ans = j
            else:
                break
        return ans
        
list1, list2 = open_file()

iii = search_index(list1,list2,tgt)
print('Search list:',location)
print('Index:',iii)