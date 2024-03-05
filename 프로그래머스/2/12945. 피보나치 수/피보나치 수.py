def solution(n):
    f0=0
    f1=1
    fn1=1
    fn2=0
    flist=[]
    flist.append(f0)
    flist.append(f1)
    for i in range(2,n+1):
        flist.append(flist[i-1]+flist[i-2])
    return flist[n]%1234567