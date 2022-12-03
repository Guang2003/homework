password = input()
rulestr = input()
rulelist = list(map(int,rulestr.split()))
rule1 = rulelist[0]
rule2 = rulelist[1]
rule3 = rulelist[2]
ans=[]


for i in password:
   
    if i.isupper():
        if ord(i)+rule2 > ord('Z'):
            ans.append(chr(ord(i)+rule2-26))
        elif ord(i)+rule2 < ord('A'):
            ans.append(chr(ord(i)+rule2+26))
        else:
            ans.append(chr(ord(i)+rule2))
    elif i.islower():
        if ord(i)+rule3 > ord('z'):
            ans.append(chr(ord(i)+rule3-26))
        elif ord(i)+rule3 < ord('a'):
            ans.append(chr(ord(i)+rule3+26))
        else:
            ans.append(chr(ord(i)+rule3))
    elif ord(i)==32:
        ans.append(i)
    else:
        if ord(i)+rule1 > ord('9'):
            ans.append(chr(ord(i)+rule1-10))
        elif ord(i)+rule1 < ord('0'):
            ans.append(chr(ord(i)+rule1+10))
        else:
            ans.append(chr(ord(i)+rule1))

for j in ans:
    print(j,end='')