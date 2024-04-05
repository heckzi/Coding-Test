n=int(input())
graph=[[0]*n for _ in range(n)]
# print(graph)
k=int(input()) #사과갯수
for _ in range(k):
    a,b=map(int,input().split())
    graph[a-1][b-1]='a'
graph[0][0]=1
l=int(input())
dir=[]
time=[]
for _ in range(l):
    temp=input().split()
    dir.append(temp[1])
    time.append(int(temp[0]))
# print(dir,time)
# print(graph)
dx=[0,1,0,-1]
dy=[1,0,-1,0] #우,하,좌,상 순이다.
t=10001
shead=[[0,0]]
diridx=0
for now in range(0,t):
    if time and now==time[0]:
        time.pop(0)
        if dir[0]=='L':
            diridx+=3
            diridx%=4
        else:
            diridx+=1
            diridx%=4
        dir.pop(0)

    x,y=shead[0][0],shead[0][1]
    nx=x+dx[diridx]
    ny=y+dy[diridx]
    if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1: #맵안에서 움직였을때
        if graph[nx][ny]=='a':#사과가 있을때
            shead.insert(0,[nx,ny])
            graph[nx][ny]=1
        else: #아무것도 없을때
            graph[nx][ny]=1
            shead.insert(0,[nx,ny])
            tail=shead.pop()
            graph[tail[0]][tail[1]]=0 #꼬리를 0으로 만들기

    else: #벽이나 몸통을 만났을때
        t=now+1
        break
print(t)
