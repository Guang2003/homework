"""
Practice 3
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""
file = open('input.txt',mode='r')#讀取測資
demo = int(file.read())#定義一個變數=讀出來的數字
file.close()#關檔案
files = open('output.txt',mode='w')#創造一個輸出文字檔
times = 1#設定執行次數
def CreatePyramid(times):#函數由下始，含本行
    for i in range(demo-1, 0, -1):#限定迴圈執行次數
        ans=(i*' ', times*'*','\n')#把輸出寫到另外的字串，方便等等寫入檔案
        times += 2#設定星號的數量，每行加二
        files.writelines(ans)#匯出成檔案
    ans=(times*'*')#因為最後一行不能有空格，所以另外寫
    times += 2
    files.writelines(ans)
    files.close()#關檔案
CreatePyramid(times)#執行函數