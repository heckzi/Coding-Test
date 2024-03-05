def solution(n):
    answer=0
    for i in range(1,n+1):
        temp=0
        add=i
        while(1):
            temp+=add
            add+=1
            if temp==n:
                answer+=1
            if temp>n:
                break
    return answer