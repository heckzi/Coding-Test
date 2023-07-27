n= list(map(int,input().split()))
sum =0
for i in range(0,len(n)):
    sum+=int(n[i]**2)
    res=sum%10
print(res)