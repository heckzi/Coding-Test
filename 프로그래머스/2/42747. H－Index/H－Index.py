def solution(citations):
    answer = 0
    # citations=[0,1,2,5,7,8,8,8,9]
    # citations=[1,10,11]
    citations.sort(reverse=True)
    for i in range(citations[0]):
        tempc=citations.copy()
        h=i
        cnt=0
        for c in citations:
            # print(h,c)
            if c>=h:
                cnt+=1
                # print("c h cnt",c,h,cnt)
        if cnt>=h:
            answer=max(h,answer)
            # print(cnt,h,answer)
    return answer
