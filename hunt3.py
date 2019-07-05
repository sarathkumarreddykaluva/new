p=[]
q=int(input())
a=list(map(int,input().split()))[:q] 
for i in range(0,q):
    if (a[i]==i):
        p.append(a[i])
        p.sort()
if(len(p)>0):
    print(*p,sep=" ")
else:
    print(-1)
