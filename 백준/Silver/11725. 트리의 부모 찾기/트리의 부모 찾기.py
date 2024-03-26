import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline()
n=int(input)
graph=[[]for _ in range (n+1)]
visited=[[0]for _ in range (n+1)]
visited[0]=1
parent=[[]for _ in range (n+1)]
for i in range(n-1):
    input=sys.stdin.readline()
    a,b=map(int,input.split())
    if a not in graph[b]: graph[b].append(a)
    if b not in graph[a]: graph[a].append(b)

def dfs(graph,n,visited):
    visited[n]=1
    for i in graph[n]:
        if visited[i]!=1:
            parent[i]=n
            dfs(graph,i,visited)
            
dfs(graph,1,visited)
for i in parent[2:]:
    print(i)