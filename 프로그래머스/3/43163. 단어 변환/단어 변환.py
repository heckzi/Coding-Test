def solution(begin, target, words):
    answer = 0
    visited=[0]*len(words)
    cnt=[]
    def linked(w1,w2):
        cnt=0
        for i in range(len(w1)):
            if w1[i]!=w2[i]:
                cnt+=1
        if cnt==1:
            return True
        else:
            return False
        
    def dfs(word,c):
        if word==target:
            cnt.append(c)
            # print("cnt",cnt)
            return
        else:
            for i in range(len(words)):
                if linked(word,words[i]) and visited[i]==0:
                    visited[i]=1
                    # print(word,words[i],c,visited)
                    dfs(words[i],c+1)
                    visited[i]=0
    dfs(begin,0)
    if cnt:
        answer=min(cnt)
    return answer