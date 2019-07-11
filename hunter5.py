p=int(input())
q=input().split()
for i in range(len(q)):
    for j in range(i+1,len(q)):
        for k in range(j+1,len(q)):
            if(int(q[i])+int(q[j])==int(q[k])):
                print(q[i],q[j],q[k])
