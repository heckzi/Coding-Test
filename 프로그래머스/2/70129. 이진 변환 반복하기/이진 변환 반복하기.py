def solution(s):
    zerocnt= 0
    zero = 0
    convcnt=0
    zeroidx=[]
    sl = list(map(int,s))
    cc=0
    while len(sl)!=1:
        for i in range (len(sl)):
            if sl[i]==0:
                zeroidx.append(i)
                zero+=1
        newlen=len(sl)-zero
        sl.clear()
        convcnt+=1
        zerocnt+=zero
        zero=0
        zeroidx.clear()
        sb = format(newlen,'b') # 1 갯수로 이진수 변환
        sl = list(map(int,sb))
    answer=[convcnt,zerocnt]
    return answer