p=int(input())
q=list(map(int,input().split()))
for i in range(p):
    if(q.count(i)==1):
        print(i)
