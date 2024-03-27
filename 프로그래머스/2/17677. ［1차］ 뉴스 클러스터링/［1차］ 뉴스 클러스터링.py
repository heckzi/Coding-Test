from collections import Counter
def solution(str1, str2):
    answer = 0
    l1=[]
    l2=[]
    str1=str1.lower()
    str2=str2.lower()
    for i in range(len(str1)):
        temp=str1[i:i+2]
        if temp.isalpha() and len(temp)==2:
            l1.append(temp)
    for j in range(len(str2)):
        temp2=str2[j:j+2]
        if temp2.isalpha() and len(temp2)==2:
            l2.append(temp2)
            
    if not l1 and not l2: # 둘다 공집합일때
        return 65536
            
    inter=list(set(l1).intersection(set(l2)))
    counter_l1=Counter(l1)
    counter_l2=Counter(l2)
    print(inter)

    final_inter=0
    final_sum=0
    for a in inter:
        final_inter+=min(counter_l1[a],counter_l2[a])

    suml=list(set(l1+l2))
    print(suml)
    for b in suml:
        final_sum+=max(counter_l1[b],counter_l2[b])
    print(final_sum,final_inter)
    answer=int((final_inter/final_sum)*65536)
    return answer