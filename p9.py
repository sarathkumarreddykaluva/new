n1,n2=map(int,input().split())
b=[]
for j in range(n1+1,n2+1):
  if j>1:
    for k in range(2,j):
      if(j%k==0):
        break
    else:
      a.append(k)
print(len(b)+1)
