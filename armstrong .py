p,q=map(int,input().split())
for m in range(p+1,q):
  sum=0
  temp1=m
  while temp1>0:
    digit=temp1%10
    sum+=digit**3
    temp1//=10
  if m==sum:
    print(m,end=' ')
