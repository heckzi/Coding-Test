def solution(people, limit):
    p=sorted(people)
    answer = 0
    length=len(p)
    hidx=length-1
    lidx=0
    while(lidx<=hidx):
        # print(p)
        if p[lidx]+p[hidx]<=limit:
            answer+=1
            hidx-=1
            lidx+=1
        else:
            hidx-=1
            answer+=1
    return answer