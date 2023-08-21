t=int(input())
a=[]
for i in range(t):
    a.append(list(map(int,input().split())))
for j in range(t):
    print(a[j][0]+a[j][1])