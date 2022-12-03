"""
Exam:E1
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""
def open_file():
    newlstnum = 0
    new_list = []
    file = open('E1_input3.txt',mode='r')
    demo = file.read()
    demolist = map(int,demo.split())
    for i in demolist:
        if newlstnum == 0:
            new_list.append(i)
            newlstnum += 1
        else:
            new_list.append(i + new_list[newlstnum - 1])
            newlstnum += 1
    file.close()
    return new_list

print('new_list =',open_file())