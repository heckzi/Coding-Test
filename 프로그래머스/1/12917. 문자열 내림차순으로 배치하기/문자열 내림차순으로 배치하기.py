def solution(s):
    answer = ''
    slist=list(s)
    upper=[]
    for i in slist:
        if i.isupper():
            slist.remove(i)
            slist.append(i)
    slist.sort(reverse=True)
    upper.sort(reverse=True)
    answer=''.join(slist)
    answer+=''.join(upper)
    return answer