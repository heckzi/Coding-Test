n,m=map(int,input().split())
graph=[[]for _ in range(n)]
visited=[0]*n

for i in range(m):
    a,b=map(int,input().split())
    if b-1 not in graph[a-1]:graph[a-1].append(b-1)
    if a-1 not in graph[b-1]:graph[b-1].append(a-1)
# print(graph,visited)

def dfs(graph,n,visited):
    visited[n]=1
    for i in graph[n]:
        if visited[i]!=1:
            # print(visited)
            dfs(graph,i,visited)

answer=0
for i in range(len(visited)):
    if visited[i]==0:
        dfs(graph,i,visited)
        # print(visited)
        answer+=1
    if sum(visited)==n:
        break
print(answer)