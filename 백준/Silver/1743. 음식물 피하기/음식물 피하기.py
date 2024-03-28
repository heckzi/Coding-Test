import sys
sys.setrecursionlimit(10000)
h,w,k=map(int,input().split())
graph=[[0]*w for _ in range(h)]
for t in range(k):
    x,y=map(int,input().split())
    graph[x-1][y-1]=1
dx=[0,0,1,-1]
dy=[1,-1,0,0]
global cnt,answer
cnt=1
answer=1
def dfs(x,y,graph):
    global cnt,answer
    graph[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
            dfs(nx,ny,graph)
            cnt+=1
            answer=max(cnt,answer)
            
clist=[]            
for i in range(h):
    for j in range(w):
        cnt=1
        if graph[i][j]==1:
            dfs(i,j,graph)
print(answer)            