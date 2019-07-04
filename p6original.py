a,b=map(str,input().split())
if len(a)!=len(b):
    print("no")
c=[a.count(i) for i in a]
d=[b.count(i) for i in b]
if (c==d):
    print("yes")
else:
    print("no")
