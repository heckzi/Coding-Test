from collections import deque
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=[]
def bfs(x,y):
    graph[x][y]=0 #여기도 방문처리 해주자
    c=1 #시작지점도 포함이니 1먼저 넣기
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >=n:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                c+=1
                queue.append((nx,ny))
    cnt.append(c)

group=0
for h in range(n):
    for w in range(n):
        if graph[h][w]==1:
            bfs(h,w)
            group+=1
print(group)
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i])