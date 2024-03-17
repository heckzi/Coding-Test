from itertools import permutations
def solution(k, dungeons):
    answer = -1
    cnt=0
    idx=[]
    for _ in range(len(dungeons)):
        idx.append(_+1)
    idx=(list(permutations(idx,len(idx))))
    for c in idx:
        dun=dungeons.copy()
        kk=k
        cnt=0
        for d in c:
            # print(c,d)
            # print(dun[d-1])
            if dun[d-1][0]<=kk:
                kk-=dun[d-1][1]
                cnt+=1
            answer=max(answer,cnt)
    return answer