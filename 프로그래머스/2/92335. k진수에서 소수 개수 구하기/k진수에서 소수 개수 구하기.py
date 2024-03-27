import math
def isprime(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def conv(n,base):
    c=''
    while n>0:
        n,mod=divmod(n,base)
        c+=str(mod)
    return c[::-1]

def solution(n, k):
    answer = 0
    convert=conv(n,k)
    # print(convert)
    l=convert.split('0')
    l=[int(v) for v in l if v]
    # print(l)
    for i in l:
        if isprime(i):
            answer+=1
    return answer