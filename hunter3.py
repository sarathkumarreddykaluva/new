p=input()
q=list(map(int,input().split()))
for i in q:
    if q.count(i)>1:
        print(i)
        break
else:
    print("unique")
