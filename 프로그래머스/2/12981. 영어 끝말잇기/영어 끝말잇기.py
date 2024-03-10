def solution(n, words):
    answer = []
    turns=[0]*n
    said=[]
    said.append(words[0])
    turns[0]=1
    who=1
    for i in range(1,len(words)):
        who+=1
        if who>n:
            who-=n
        turns[who-1]+=1
        if words[i] not in said:
            said.append(words[i])
        else:
            break
            
        if said[i-1][-1]!=words[i][0]:
            break

    answer.append(who)
    answer.append(turns[who-1])
    print(said)
    if len(words)==len(said):
        answer=[0,0]
    return answer