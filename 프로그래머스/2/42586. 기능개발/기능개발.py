def solution(progresses, speeds):
    answer = []
    release = 0
    while progresses:
        if progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            release +=1
        else:
            if release!=0:
                answer.append(release)
                release=0
            for i in range(len(progresses)):
                progresses[i]+=speeds[i]
    if release !=0:
        answer.append(release)
    return answer