def solution(n, results):
    answer = 0
    graph=[[0 for _ in range(n+1)] for _ in range(n+1)] #누구한테 졌는지 들어가있음
    for _ in range(len(results)):
        win=results[_][0] #이긴 선수의 인덱스
        lose=results[_][1] #진 선수
        graph[win][lose]=1
        graph[lose][win]=-1
    # print(graph)
    
    for k in range(1,n+1): #경유점 
        for i in range(1,n+1): #시작점
            for j in range(1,n+1): #도착점
                if graph[i][j]==0:
                    # print(i,j,graph[i][j])
                    if graph[i][k] ==1 and graph[k][j]==1:
                        graph[i][j]=1
                    if graph[i][k] ==-1 and graph[k][j]==-1:
                        graph[i][j]=-1                       
                    
    # print(graph)
    for i in graph:
        if i.count(0)==2:
            answer+=1
    return answer