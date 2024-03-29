def solution(babbling):
    answer = 0
    words=["aya", "ye", "woo", "ma"]
    for b in babbling:
        for w in words:
            b=b.replace(w,' ')
            # print(b,w)
        b=b.replace(' ','')
        if b=='':
            answer+=1
    return answer