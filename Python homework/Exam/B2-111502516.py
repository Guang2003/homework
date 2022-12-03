"""
Bonus 02
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""

def print_dec(demo):
    wait = []
    if first == '0':
        power = int(0)
        dec_num = 0
        for i in demo[::-1]:
            dec_num += (2**power)*int(i)
            power += 1
        return dec_num
    else:
        for i in demo[1:]:
            if i == '0':
                wait.append('1')
            else:
                wait.append('0')
        result = ''.join(wait)
        power = int(0)
        dec_num = 0
        for i in result[::-1]:
            dec_num += (2**power)*int(i)
            power += 1
            #print('b')
        return dec_num+1

def dec_reverse(num):
    num = str(num)
    new_num = []
    result = ''
    for i in num:
        new_num.append(i)
    new_num.reverse()
    result = ''.join(new_num)
    if result[0] == '0' and len(result)!= 1:
        return result[1]
    return result
    
def print_hex(demo):
    hex_num = '0'
    result = []
    while demo != 0:
        if demo%16 < 10:
            result.append(demo % 16)
            demo = (demo // 16)
        else:
            if demo%16 == 10:
                result.append('a')
            elif demo%16 == 11:
                result.append('b')
            elif demo%16 == 12:
                result.append('c')
            elif demo%16 == 13:
                result.append('d')
            elif demo%16 == 14:
                result.append('e')
            else:
                result.append('f')
            demo = (demo // 16)
    result.reverse()
    if result == []:
        result = [0]
    result = map(str,result)
    hex_num = ''.join(result)
    return hex_num

def Input_type(num) :
    for i in num:
        if i != '0' and i != '1':
            print('Input number is not binary')
            return False
    return True

def Output( decimal, decimal_reverse ,heximal ) :
  print("Decimal:", decimal)
  print("Decimal reverse:", decimal_reverse)
  print("Heximal:", heximal)

while 1:
    number = input("Please input the binary : ")
    if number == '-1':
        break
    first = number[0]
    if Input_type(number):
        Output(print_dec(number),dec_reverse(print_dec(number)),print_hex(print_dec(number)))