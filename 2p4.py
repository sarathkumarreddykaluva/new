n=int(input())
s=list(input())
l=['a','e','i','o','u']
p=[]
for i in s:
	if i not in l:
		p.append(i)
p=p[::-1]
print(''.join(p))
