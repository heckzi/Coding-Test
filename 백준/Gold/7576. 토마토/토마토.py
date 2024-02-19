# -*- coding: utf-8 -*-
from collections import deque
import sys
input = sys.stdin.readline()
m,n =map(int,input.split())

graph=[]
for i in range(n):
    input = sys.stdin.readline()
    graph.append(list(map(int,input.split())))
# print(graph)

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:#익은 토마토 위치만 체크
            queue.append([i,j])

dx = [-1,1,0,0] # 상 하 좌 우
dy = [0,0,-1,1]
def bfs():
    while queue:
        x,y = queue.popleft() #현재 위치 방문 후 빼주기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 0:#창고를 벗어나지 않고 안익은 토마토면
                graph[nx][ny]=graph[x][y]+1 #날짜를 누적해가면서 더함
                queue.append((nx,ny)) #새로운 익은 토마토 추가
day = 0
bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
        else:
            day = max(day,max(i))

print(day-1) #시작 날짜를 1로 했으므로 -1해서 출력
