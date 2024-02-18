# -*- coding: utf-8 -*-
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]= True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

if __name__=="__main__":
    graph = []
    c, l ,v = map(int,input().split())
    # print(c,l,v)
    for i in range(c+1):
        graph.append([])
    for i in range(1,l+1):
        a,b=map(int,input().split())
        if b not in graph[a]:
            graph[a].append(b)
        if a not in graph[b]:
            graph[b].append(a)
    for i in range(c+1):
        graph[i].sort()
    visited = [False]*(c+1)
    dfs(graph, v, visited)
    print('')
    visited2 = [False]*(c+1)
    bfs(graph, v, visited2)
