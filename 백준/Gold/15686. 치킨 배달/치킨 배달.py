n,m=map(int,input().split())
graph=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    graph.append(temp)

chicken=[]
house=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chicken.append((i,j))
        if graph[i][j]==1:
            house.append((i,j))

from itertools import combinations
nomi=list(combinations(chicken,m))
answer=100000
for no in nomi:
    citydist=0
    for h in house:
        mindist=100000
        for c in no:
            mindist=min(mindist,abs(h[0]-c[0])+abs(h[1]-c[1]))
        citydist+=mindist
    answer=min(answer,citydist)
print(answer)