n1,n2=map(list,input().split())
cou=0
if(len(n1)==len(n2)):
    for i in range(0,len(n1)):
        if(n1[i]==n2[i]):
            continue
        else:
            cou=cou+1
if(cou==1):
    print("yes")
else:
    print("no")
