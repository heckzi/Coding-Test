def solution(n):
    answer = 1
    x=1
    while(1):
        # print(answer,x)
        if answer==n+1:
            break
        if x%3==0 or '3' in list(str(x)):#저주숫자에 걸리면
            x+=1
            continue
        else:
            answer+=1
            if answer==n+1:
                break
            x+=1

    return x