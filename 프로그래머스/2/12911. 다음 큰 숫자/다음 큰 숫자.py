def solution(n):
    answer = 0
    cnt=0
    bin = format(n,'b')
    for i in list(bin):
        if i =='1':
            cnt+=1
    next=n
    nextcnt=0
    while(1):
        next+=1
        nextbin=format(next,'b')
        # print(next,cnt,nextcnt,bin,nextbin)
        for j in list(nextbin):
            if j =='1':
                nextcnt+=1
        if nextcnt==cnt:
            answer=next
        else:
            nextcnt=0
        if answer!=0:
            break
    return answer