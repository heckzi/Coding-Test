from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q=deque()
    for i in range(len(cities)):
        if cities[i].lower() not in q:
            answer+=5
            q.append(cities[i].lower())
        else:
            answer+=1
            q.remove(cities[i].lower())
            q.append(cities[i].lower())
        if len(q)>cacheSize:
            q.popleft()
        # print(q)
        
    return answer