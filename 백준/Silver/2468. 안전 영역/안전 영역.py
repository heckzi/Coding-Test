n=int(input())
graph=[]
max_h=0
for i in range(n):
    l=list(map(int,input().split()))
    max_h=max(max_h,max(l))
    graph.append(l)
# print(graph)

dx=[0,0,1,-1]
dy=[1,-1,0,0]
from collections import deque
def bfs(x,y,graph):
    graph[x][y]=0
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=0:
                graph[nx][ny]=0
                q.append((nx,ny))

cnt=[]
import copy
from pprint import pprint
for h in range(max_h+1):
    c=0
    temp_h=max_h-h
    temp_graph=copy.deepcopy(graph)
    for i in range(len(temp_graph)):
        for j in range(len(temp_graph[i])):
            if (temp_graph[i][j]-temp_h)<=0:
                temp_graph[i][j]=0
            else: temp_graph[i][j]-=temp_h
    # pprint(temp_graph)
    for x in range(n):
        for y in range(n):
            if temp_graph[x][y]!=0:
                bfs(x,y,temp_graph)
                c+=1
    cnt.append(c)
print(max(cnt))