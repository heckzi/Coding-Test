import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    if scoville :
        while scoville[0] < K:
            # print(1,scoville)
            new=heapq.heappop(scoville)+(heapq.heappop(scoville)*2)
            heapq.heappush(scoville,new)
            answer+=1
            if len(scoville) == 1:
                if scoville[0] < K:
                    answer = -1
                    break
    return answer