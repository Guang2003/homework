"""
Assignment 3
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
"""
file = open('input.txt',mode='r') #開啟並讀取檔案到file這個變數
demo = int(file.read())
file.close()
files = open('output.txt',mode='w')
num = 0 #定義之後在畫金字塔時要充當計數器用的變數
times = 2
stepmax = 0
def isPrime(num):#質數檢測函數
    for i in range(2, num):
        if  (num % i) ==0:
            return 'N'
    return 'Y'
def CreatePyramid(times):#畫金字塔函數
    ans=((demo-1)*' ','1')
    files.writelines(ans)
    if demo != 1:
        ans=('\n')
        files.writelines(ans)
    num = 2
    for i in range(demo-2, 0, -1):
        stepmax = times**2
        times+=1
        ans = (i*' ')
        files.writelines(ans)
        while num <= stepmax:
            ans = (str(isPrime(num)))#把該編號的數字透過質數檢測函數轉化成Y/N
            files.write(ans)
            num += 1
        ans=('\n')
        files.writelines(ans)
    stepmax = times**2
    while demo != 1 and num <= stepmax:#最後一行為了避免多輸出一個空格故拉出來單獨跑
        ans = (str(isPrime(num)))
        files.write(ans)
        num += 1
CreatePyramid(times)#執行函數並關閉檔案
files.close()