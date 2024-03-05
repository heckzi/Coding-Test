def solution(n):
    sn=str(n)
    answer = []
    for i in range(len(sn)):
        answer.append(sn[-(1+i)])
    answer=list(map(int,answer))
    return answer