"""
Assignment 4
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
"""
demolist = []#定義一些之後要用的東西
exit_cmd = 0
factor_list = []
with open('Input.txt','r') as file:#開檔把東西讀出來
    for line in file:
        demolist.append(line.split()[-1])

def num_exist(number):#檢測是否存在於測資內的函數
    if str(number) in demolist:
        return True
    return False

def find_factor_num( number ): #檢測有幾個因數並輸出因數列表
    factor_num = 0
    for i in range(1,number+1):
        if (number%i) ==0:
            factor_num +=1
            factor_list.append(i)
    return factor_num

def find_prime_num():#把因數列表裡的數字抓來檢查是不是質數
    prime_num = 0
    for i in factor_list:
        if i == 2:
            prime_num += 1
        for j in range(2,i):
            if  (i % j) ==0:
                break
            elif j == (i-1):
                prime_num += 1
                break
            else:
                continue
    return prime_num

while exit_cmd < 10:#主程式
    factor_list=[]
    if exit_cmd < 10:
        num = (input('Input the number to check exist or exit : '))
        if num == 'exit':
            exit_cmd = 10000000000000
        else:
            num = int(num)
            if num_exist(num) == False:
                print('Number_'+ str(num) + ' is not exist, please input a new number or input "exit" to leave program')
            else:
                print('Number_' + str(num) + ' exists in the document and the number of factor is', find_factor_num(num) , 
                'and the number of prime is',  find_prime_num())
                print('Please input the next number or input "exit" to leave')