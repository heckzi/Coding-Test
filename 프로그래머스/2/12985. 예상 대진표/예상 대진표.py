def solution(n,a,b):
    answer = 0
    # n,a,b= 8,4,5
    round = 1
    if abs(a-b)==1:
        if max(a,b)%2==0:
            return 1
        # else:
        #     return 2
    # print(abs(a-b),abs(a-b)!=1 and max(a,b)%2!=0,abs(a-b)!=1,max(a,b)%2!=0 )
    while(1):
        # print(round,a,b,abs(a-b))
        if a%2==0: #짝수이면
            a/=2
            round+=1
        else: #홀수이면
            if a==1:
                a=1
                round+=1
            else:
                a=a/2+0.5
                round+=1
        
        if b%2==0: #짝수이면
            b/=2
        else:
            if b==1:
                b=1
            else:
                b=b/2+0.5
        if a==b:
            break
    answer=round-1
    return answer