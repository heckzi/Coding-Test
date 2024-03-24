h,w=map(int,input().split())
graph=[]
for _ in range(h):
    graph.append(list(input()))
# print(graph)

from collections import deque
dx=[0,0,1,-1]
dy=[-1,1,0,0]
global ans
ans=0
def bfs(x,y):
    global ans
    queue=deque()
    queue.append((x,y))
    visited=[[0]*w for _ in range(h)]
    visited[x][y]=1
    max_dist=0            
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if visited[nx][ny]==0 and graph[nx][ny]=='L':
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx,ny))
                    max_dist=max(max_dist,visited[nx][ny])
    ans=max(ans,max_dist)
    
for i in range(h):
    for j in range(w):
        if graph[i][j]=='L':
            bfs(i,j)
print(ans-1)
