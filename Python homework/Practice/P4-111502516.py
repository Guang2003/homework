"""
Practice 4
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""
file = open('Input.txt',mode='r')#開啟檔案並設定模式為讀取
demo = file.read()#將測資儲存在變數demo
demolist = map(int,demo.split(' '))#將字串內的數字以空格為間隔切割成element並以list儲存在demolist
file.close()#停止讀取，關閉檔案
files = open('Output.txt',mode='w')#開啟等等要寫入的目標檔案
item_num = 1#計數器
def find_factor( num ): #找因數的函數
    if (i%num) ==0:
        return num

def find_prime( num ):#判斷是否為質數的函數
    if num == 1:
        return 'F'
    for i in range(2, num):
        if  (num % i) ==0:
            return 'F'
    return 'T'

for i in demolist:#主程式
    files.write('Number_')
    files.write(str(item_num))
    files.write(': ')
    files.write(str(i))
    files.write('\n')
    item_num += 1
    for j in range(1,i+1):#到i+1才會包含i本身
        if type(find_factor(j)) == int:
            files.write(str(find_factor(j)))
            files.write(' ')
            files.write(find_prime(find_factor(j)))
            files.write('\n')

files.close()#寫入完成，關閉檔案