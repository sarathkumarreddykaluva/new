p=int(input())
q=list(map(int,input().split()))
m1=max(q)
a,b=0,0
for i in range(0,len(q)-1):
  for j in range(i+1,len(q)):
    if abs(q[i]+q[j])<m1:
      a,b=q[i],q[j]
      m1=abs(a+b)
print(a,b)
