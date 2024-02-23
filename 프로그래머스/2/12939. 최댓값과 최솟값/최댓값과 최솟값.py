def solution(s):
    intlist= list(map(int,s.split(' ')))
    answer = str(min(intlist)) + " " +str(max(intlist))
    return answer