def solution(n):
    answer = []
    sn=str(n)
    for i in range(len(sn)):
        answer.append(sn[i])
    answer.sort(reverse=True)
    answer=int(''.join(answer))
    return answer