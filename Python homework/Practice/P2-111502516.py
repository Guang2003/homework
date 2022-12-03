"""
Practice 2
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""
z=0
while z<1:
    
    if z<1:
        cmd = input('Please enter your password: ')
        if cmd=='exit':
            z=999
        else:
            
            while True:
                if len(cmd) <6 or len(cmd) > 10:
                    a=0
                    break
                else:
                    a=1
                break

            while True:
                for i in cmd:
                    if 64 < ord(i) < 91:
                        b=1
                        break
                    else:
                        b=0  
                break

            while True:
                for i in cmd:
                    if 47 < ord(i) < 58:
                        c=1
                        break
                    else:
                        c=0
                break

            while z< 100:
                if cmd == 'exit':
                    break
                elif a ==0:
                    print('Password should contain 6 to 10 characters, try again or type "exit" to leave.')
                    break
                elif b ==0:
                    print('Password should contain at least one upper-case alphabetical character, try again or type "exit" to leave.')
                    break
                elif c ==0:
                    print('Password should contain at least one number, try again or type "exit" to leave.')
                    break
                else:
                    print('Password is valid.')
                    z = 999
                    break
    else:
        break