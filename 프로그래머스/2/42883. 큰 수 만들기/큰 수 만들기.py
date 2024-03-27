# from itertools import combinations
# def solution(number, k):
#     answer = ''
#     number=str(number)
#     l=[v for v in number]
#     nomi=list(combinations(l,len(number)-k))
#     final=[]
#     for i in nomi:
#         final.append(int(''.join(i)))
#     answer=str(max(final))
#     return answer
def solution(number, k):
    s=[]
    for n in number:
        while s and s[-1]<n and k>0:
            s.pop()
            k-=1
        s.append(n)
    if k!=0:
        s=s[:-k]
    return ''.join(s)