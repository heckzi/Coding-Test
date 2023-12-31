def solution(participant, completion):
    sumhash=0
    hashDic={}
    for p in participant:
        hashDic[hash(p)]=p
        sumhash+=hash(p)
    for c in completion:
        sumhash-=hash(c)
    return hashDic[sumhash]