num = int(input())
t = list(map(int,input().split()))
t.sort()
a = []
for i in range(len(t)-1):
    if t[i]==t[i+1]:
        a.append(t[i])
if a:
    for x in  set(a):
        print(x,end=" ")
else:
    print("unique")
