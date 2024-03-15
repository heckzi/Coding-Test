def dfs(graph,node,visited):
    visited[node]=True
    for i in graph[node]:
        if not visited[i]:
            dfs(graph,i,visited)
            
def solution(n, computers):
    graph=[[]for _ in range(n)]
    for c in range(len(computers)):
        for j in range(n):
            if computers[c][j] ==1:
                if j not in graph[c] and j!=c:
                    graph[c].append(j)
    print(graph)
    answer = 0
    visited=[False]*n
    for l in range(n):
        if visited[l]==False:
            dfs(graph,l,visited)
            answer+=1
            if sum(visited)==n:
                break
    return answer