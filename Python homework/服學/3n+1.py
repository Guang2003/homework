num = int(input())
if num%2 == 0:
    num = num/2
else:
    num = num*3+1
def hehehe(demo):
    
    if demo == 1:
        print(int(demo))
        return 0
    elif demo%2 == 0:
        print(int(demo))
        hehehe(demo/2)
    else:
        print(int(demo))
        hehehe(3*demo+1)
hehehe(num)