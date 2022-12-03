"""
Exam 3
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