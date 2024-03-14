n=int(input())
line=int(input())

def dfs(graph,node,visited):
    visited[node]= True
    # print(node,end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(graph,i,visited)

graph=[[]for _ in range(n)]
for i in range(line):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    set(graph[a-1])
    set(graph[b-1])

visited=[False]*n

dfs(graph,0,visited)
cnt=0
for v in visited:
    if v==True:
        cnt+=1

print(cnt-1)