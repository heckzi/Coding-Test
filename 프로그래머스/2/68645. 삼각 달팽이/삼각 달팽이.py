def solution(n):
    answer = []
    dx=[0,1,-1]
    dy=[1,0,-1]
    for h in range(1,n+1):
        answer.append([0]*h)
    start=1
    x,y,i=0,0,0
    while(1):
        answer[y][x]=start
        
        nx=x+dx[i]
        ny=y+dy[i]
        if nx==n or ny==n or answer[ny][nx]!=0:
            i=(i+1)%3
            nx=x+dx[i]
            ny=y+dy[i]
            if nx==n or ny==n or answer[ny][nx]!=0:
                break
        start+=1
        x,y=nx,ny
    
    final=[]
    for _ in range(len(answer)):
        final+=answer[_]
    return final