n,m=map(int,input().split())
graph=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    graph.append(temp)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def virus(x,y,graph):
    graph[x][y]=2
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==0:
                virus(nx,ny,graph)

from itertools import combinations
nomi=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            nomi.append([i,j])
wall=list(combinations(nomi,3))

answer=0
import copy

for w in wall:
    temp=copy.deepcopy(graph)
    for a in w:
        temp[a[0]][a[1]]=1
    # pprint(temp)
    now=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==2:
                virus(i,j,temp)
    for q in range(n):
        for w in range(m):
            if temp[q][w]==0:
                now+=1

    answer=max(answer,now)
print(answer)