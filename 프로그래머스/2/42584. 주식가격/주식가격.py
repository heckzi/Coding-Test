def solution(prices):
    answer = []
    stack=[]
    
    for i in range(len(prices)):
        stack.append(prices[i])
        cnt=-1
        for j in range(i,len(prices)):
            cnt+=1
            if stack[-1]>prices[j]:
                stack.pop()
                break
        answer.append(cnt)
    return answer