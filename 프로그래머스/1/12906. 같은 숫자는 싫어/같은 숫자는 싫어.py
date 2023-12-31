def solution(arr):
    answer = []
    idx=0
    answer.append(arr[0])
    for i in arr:
        if answer[idx]==i:
            continue
        else:
            answer.append(i)
        idx+=1
    return answer