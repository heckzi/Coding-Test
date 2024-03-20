n=int(input())
a=[]
b=[]
for i in range(n):
    temp=list(map(int,input().split()))
    a.append(temp)
for j in range(n):
    temp=list(map(int,input().split()))
    b.append(temp)

def left(a):
    l_a=[]
    for i in range(n):
        temp=[]
        for j in range(i,n):
            # print(j,i,a[j][i])
            temp.append(a[j][i])
        l_a.append(temp)
    l_a.reverse()
    return l_a

def right(a):
    return left(left(a))

import copy
def rev(a):
    r_a=copy.deepcopy(a)
    for j in r_a:
        j.reverse()
    return r_a

# print(a)
# print(a,rev(a))

answer=1000000000
caselist=[a,left(a),right(a),left(rev(a)),right(rev(a)),rev(a)]
for c in caselist:
    cnt=0
    for i in range(n):
        for j in range(len(c[i])):
            if c[i][j]!=b[i][j]:
                cnt+=1
    answer=min(answer,cnt)

print(answer)
