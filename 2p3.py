n=int(input(""))
count=0
while((n!=0)and(n<=1000000000000000000)):
    r=n%10
    count+=pow(r,2)
    n//=10
print(count)
