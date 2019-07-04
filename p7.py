m=input()
n=list(m)
n[::2],n[1::2]=n[1::2],n[::2]
''.join(n)
print(*n,sep="")
