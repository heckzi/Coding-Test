def solution(sizes):#w,h
    w=[]
    h=[]
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:#w가 더 작으면
            temp = sizes [i][0]
            sizes[i][0]=sizes[i][1]
            sizes[i][1]=temp#바꾸기
        w.append(sizes[i][0])
        h.append(sizes[i][1])
    answer=max(w)*max(h)
    return answer