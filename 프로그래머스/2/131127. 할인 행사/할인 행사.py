def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        temp_n=number.copy()
        if len(discount[i:10+i])==10:
            dis=discount[i:10+i]
            # print(dis)
            for j in dis:
                if j in want:
                    idx=want.index(j)
                    # print("j","idx","want[idx]","number[idx]",j,idx,want[idx],number[idx])
                    if temp_n[idx]>0:
                        temp_n[idx]-=1
                        # print("뺀다",want[idx],number)
        if sum(temp_n)==0:
            answer+=1
    return answer