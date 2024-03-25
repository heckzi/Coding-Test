from collections import deque
dx=[0,1,0,-1,1,1,-1,-1]
dy=[1,0,-1,0,1,-1,-1,1]
def bfs(x,y):
    q=deque()
    graph[x][y]=0
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append((nx,ny))
while True:
    w,h=map(int,input().split())
    if (w,h)==(0,0):
        break
    graph=[]
    for r in range(h):
        row=list(map(int,input().split()))
        graph.append(row)
    cnt=0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)
