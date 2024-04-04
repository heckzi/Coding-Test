import math
def is_prime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=int(input())
nlist=list(map(int,input().split()))
cnt=0
for i in range(n):
    if is_prime(nlist[i]):
        cnt+=1
        
print(cnt)