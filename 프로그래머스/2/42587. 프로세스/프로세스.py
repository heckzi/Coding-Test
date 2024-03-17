from collections import deque
def solution(priorities, location):
    # priorities=[1, 1, 2, 3, 2, 1]
    # location=0
    answer = 0
    q=deque(priorities)
    arr=[]
    idx=deque()
    for _ in range(len(q)):
        idx.append(_)
    while(q):
        temp=q.popleft()
        tempidx=idx.popleft()
        if any (temp<j for j in q):
            q.append(temp)
            idx.append(tempidx)
        else:
            arr.append(tempidx)
            # print(arr)
    answer=arr.index(location)+1
    return answer