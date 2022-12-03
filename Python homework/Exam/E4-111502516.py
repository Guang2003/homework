"""
Exam 4
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""
def open_file():
    file = open('E4_input.txt',mode='r')
    demo = file.read()
    file.close()
    return int(demo)
userans = int(input())
def check_number(num):
    if num == userans:
        return True
    return False
print(open_file())
print(check_number(open_file()))