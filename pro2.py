a1=int(input())
k=[]
for i in range (0,a1):
    k.append(input())
l1=len(k[0])
e1=""
for i in range (0,l1):
    c=k[0][i]
    f=0
    for j in range (0,a1):
        if(c!=k[j][i]):
            f=1
    if(f==0):
        e1=e1+c
    else:
        break
print(e1)
