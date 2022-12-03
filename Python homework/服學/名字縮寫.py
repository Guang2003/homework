limit=int((input()))

name=input()

if len(name)<= limit or limit<5:
    print(name)

else:
    print(name[0],name[1],(len(name)-3),name[-1],sep = "")