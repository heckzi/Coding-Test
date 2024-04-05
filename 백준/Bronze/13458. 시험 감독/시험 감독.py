n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())

total=n

for room in range(n):
    a[room]-=b
    if a[room]>0:
        if a[room]%c==0:
            total+=a[room]/c
        else:
            total+=a[room]//c+1
            # print(a)
print(int(total))