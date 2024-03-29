import copy
def solution(board):
    answer = 0
    temp=copy.deepcopy(board)
    n=len(board)
    dx=[0,0,1,-1,1,1,-1,-1]
    dy=[1,-1,0,0,1,-1,1,-1]
    for h in range(n):
        for w in range(n):
            if board[h][w]==1:
                # print(h,w)
                for i in range(8):
                    nx=h+dx[i]
                    ny=w+dy[i]
                    if 0<=nx<n and 0<=ny<n:
                        temp[nx][ny]=1
    # print(*temp,sep='\n')
    for t in temp:
        answer+=sum(t)
    return n**2-answer