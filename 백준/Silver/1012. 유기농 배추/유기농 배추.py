t=int(input())
answer=[]
for _ in range(t):
    w,h,n=map(int,input().split())
    graph=[[0]*w for _ in range(h)]
    for i in range(n):
        x,y=map(int,input().split())
        graph[y][x]=1

    from collections import deque
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    def bfs(x,y):
        queue=deque()
        queue.append((x,y))
        graph[x][y]=0
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
                    graph[nx][ny]=0
                    # print(*graph,sep='\n')
                    # print('\n')
                    queue.append((nx,ny))

    ans=0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(i,j)
                ans+=1
    answer.append(ans)
for a in range(len(answer)):
    print(answer[a])