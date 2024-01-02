def solution(n, lost, reserve):
    real_r = []
    for i in reserve:
        if i not in lost:#여분이 있고 도난도 안당한 경우
            real_r.append(i)
        else: #여분이 있고 도난당한 경우
            lost.remove(i)
            
    part=n-len(lost)
    lost.sort()
    for j in range(len(lost)):
        if lost[j]-1 in real_r:
            real_r.remove(lost[j]-1)
            part+=1
        elif lost[j]+1 in real_r:
            real_r.remove(lost[j]+1)
            part+=1

    answer = part
    return answer