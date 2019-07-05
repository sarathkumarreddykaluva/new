    
p=str(input())
d={}

for i in p:
    if i not in d.keys():
        d[i]=p.count(i)
print(max(d, key=d.get))
