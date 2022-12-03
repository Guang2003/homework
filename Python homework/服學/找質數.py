fuckyou = int(input())
def isPrime(num):
    if num-1 ==2:
        return 2
    for j in range(num-1,1,-1):
        #print(j)
        for i in range(2, j):
            if  (j % i) ==0:
                break
        else:
            return j
print(isPrime(fuckyou))