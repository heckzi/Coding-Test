from itertools import combinations
import math
def solution(n):
    answer = 0
    cnt=0
    if n==1:
        return 1%1234567
    if n==2:
        return 2%1234567
    if n%2==0: #짝수면
        answer+=2 #1칸만,2칸만 가는경우
        while(1):
            n-=2
            cnt+=1 #2갯수
            if n==2:
                break
        for i in range(cnt):
            answer+=math.comb(cnt+2+i,cnt-i)
    else: #홀수면
        answer+=1 #1칸만 가는경우
        while(1):
            n-=2
            cnt+=1
            if n==1:
                break
        for i in range(cnt):
            # print("i,comb,answer,cnt",i,math.comb(cnt+1+i,cnt-1+i),answer,cnt)
            answer+=math.comb(cnt+1+i,cnt-i)
    return answer%1234567