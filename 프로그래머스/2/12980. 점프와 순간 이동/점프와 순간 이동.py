def solution(n):
    ans = 0
    if n==1:
        return 1
    while(1):
        if n%2==0:
            n/=2
        else:
            n-=1
            ans+=1
        if n==0:
            break
    return ans