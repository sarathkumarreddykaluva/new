m,n=map(str,input().split())
if len(m)!=len(n):
    print("no")
x=[m.count(i) for i in m]
y=[n.count(i) for i in n]
if (x==y):
    print("yes")
else:
    print("no")
