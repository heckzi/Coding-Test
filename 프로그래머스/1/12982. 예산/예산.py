def solution(d, budget):
    answer = 0
    for i in range(len(d)):
        if budget<min(d) or not d:
            break
        budget-=min(d)
        # print(budget,d,min(d))
        d.remove(min(d))
        answer+=1

    return answer