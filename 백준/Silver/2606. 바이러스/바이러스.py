n=int(input())
l=int(input())
graph=[[]for _ in range(n)]
for _ in range(l):
    a,b=map(int,input().split())
    if b-1 not in graph[a-1]:
        graph[a-1].append(b-1)
    if a-1 not in graph[b-1]:
        graph[b-1].append(a-1)

def dfs(n,graph,visited):
    visited[n]=True
    for i in graph[n]:
        if not visited[i]:
            dfs(i,graph,visited)

visited=[False]*n
dfs(0,graph,visited)
# print(visited)
print(sum(visited)-1)