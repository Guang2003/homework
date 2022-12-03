"""
Assignment 8
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
"""
def preprocess():
    with open('input.txt', 'r') as file:
        # 額外補充：map(function, iterable) 將iterable中的每個物件以function做處理並回傳sequence
        #          在這裡就是將int()作為function,將從檔案中讀出的list作為iterable
        #          由於回傳的是sequence 因此需要list()來強制轉換
        #          帥氣度破表
        data = list(map(int, file.read().split()))
    return data

def bubble(demo):
    lenth = len(demo)
    count = 1
    for i in range(lenth-1):
        for j in range(lenth-i-1):
            if demo[j]>demo[j+1]:
                demo[j],demo[j+1] = demo[j+1],demo[j]
        print('第',count,'次',demo)
        count += 1
    return demo

def showlist(count, listname):
    print('第', count, '次', listname)

def show_original(listname):
    print('原資料：', listname)
bubble(preprocess())
show_original(preprocess())