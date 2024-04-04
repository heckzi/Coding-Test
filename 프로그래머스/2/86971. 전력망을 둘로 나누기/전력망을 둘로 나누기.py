def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
import copy
def solution(n, wires):
    answer = 100
    cnt=len(wires)
    for t in range(cnt):
        temp=wires[t]
        temp_wires=copy.deepcopy(wires)
        temp_wires.remove(temp)
        graph=[[]for _ in range(n)]
        for w in temp_wires:
            a=w[0]-1
            b=w[1]-1
            if a not in graph[b]:
                graph[b].append(a)
            if b not in graph[a]:
                graph[a].append(b)
                
        # print(temp_wires,graph)
        visited=[False]*n
        dfs(graph,temp[0]-1,visited)
        first=sum(visited)
        visited=[False]*n
        dfs(graph,temp[1]-1,visited)
        second=sum(visited)
        # print(first,second)
        answer=min(answer,abs(first-second))
        
    return answer