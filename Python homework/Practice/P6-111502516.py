"""
Practice 6
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""


def print_dec(demo):
    power = int(0)
    dec_num = 0
    for i in demo[::-1]:
        dec_num += (2**power)*int(i)
        power += 1
    print("NUM(DEC) : {}".format(dec_num))#format function will replace the "{}" with given variables, you can google it for the detail


def print_err_msg(demo):
    for i in demo:
        if not(48 <= ord(i) <= 49):
            err_msg = "Not Binary Number!"
            print(err_msg)
            return False
    return True
    

number = input("NUM(BIN) : ")
if print_err_msg(number):
    print_dec(number)
# write your code form here...

# if input is not binary number, like "abc","7789", use print_err_msg() to print msg.

# do not use "int(number,2)"

# ...to here