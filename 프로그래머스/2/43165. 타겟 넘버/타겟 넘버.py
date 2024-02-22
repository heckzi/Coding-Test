from itertools import combinations
def solution(numbers, target):
    count =0
    idx =[]
    for i in range(len(numbers)):
        idx.append(i)
    
    for i in range(1,len(numbers)+1):
        idxlist=list(combinations(idx,i))
        temp = numbers.copy()
        for j in idxlist:
            for k in j: #temp에 있는거 각 인덱스에 맞게 - 붙히기
                temp[k]*=-1
            # print('j',j,'k',k,'temp',temp,'sum',sum(temp))
            if sum(temp)==target:
                count+=1
            temp= numbers.copy()
    # print('count',count)
    return count