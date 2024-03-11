def solution(k, tangerine):
    answer = 0
    c=[0]*max(tangerine)
    for i in tangerine:
        c[i-1]+=1
    c.sort()
    # print(c)
    for i in range(len(c)):
        k-=c[-(1+i)]
        answer+=1
        if k<=0:
            break
    return answer