n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
for i in range(0,n1[1]):
  n2=[n2[-1]] + n2[:-1]
print(*n2,end=' ')
