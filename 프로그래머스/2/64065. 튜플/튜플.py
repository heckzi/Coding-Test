def solution(s):
    answer = []
    s=s[1:-1]
    slist=s.split('},{')
    for i in range(len(slist)):
        slist[i]=slist[i].replace('{','')
        slist[i]=slist[i].replace('}','')
        slist[i]=slist[i].replace('}','')
        slist[i]=slist[i].split(',')
    
    n=len(slist)
    for length in range(1,n+1):
        for i in range(n):
            if len(slist[i])==length:
                answer.append(slist[i])
    final=[]
    for _ in range(len(answer)):
        final+=answer[_]
    final=list(map(int,final))
    answer=[]
    for f in final:
        if f not in answer:
            answer.append(f)
    return answer