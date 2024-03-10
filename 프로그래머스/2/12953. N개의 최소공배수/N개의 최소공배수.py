def solution(arr):
    answer=2
    okay=True
    while(1):
        for a in arr:
            okay=True
            if answer%a!=0:
                # print("dfd2",answer,a,answer%a)
                answer+=1
                okay=False
                break
        if okay:
            # print("dfd3",answer,a,answer%a)
            return answer
