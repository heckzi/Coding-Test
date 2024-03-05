def solution(n):
    answer = 0
    ilist=[]
    for i in range(1,int(n/2)):
        if n%i==0:
            print(i,n/i)
            if n/i!=i:
                if not i in ilist:
                    ilist.append(i)
                    ilist.append(n/i)
            else:
                if not i in ilist:
                    ilist.append(i)
    answer=sum(ilist)
    if n==1:
        answer =1
    return answer