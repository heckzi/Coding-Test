def solution(s):
    answer = ''
    print((len(s)/2)%2)
    if len(s)==1:
        return s
    if len(s)%2==0:
        answer=s[len(s)//2-1]+s[len(s)//2]
        print("짝",answer)
    else:
        answer=s[len(s)//2]
        print("홀",answer)
    return answer