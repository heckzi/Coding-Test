def solution(brown, yellow):
    answer = []
    # brown,yellow=12,4
    ys=[]
    for i in range(1,yellow+1):
        if yellow%i==0 :
            if i not in ys:
                ys.append(i)
    for i in range(int(len(ys)/2)+1):
        if ((ys[-(1+i)]+2)*2 + (2*ys[i]))==brown and ys[-(1+i)]>=ys[i]:
            answer.append(ys[-(1+i)]+2)
            answer.append(ys[i]+2)
            # print(int(len(ys)/2)+1,i,answer)
    if yellow==1:
        answer=[3,3]
    return answer