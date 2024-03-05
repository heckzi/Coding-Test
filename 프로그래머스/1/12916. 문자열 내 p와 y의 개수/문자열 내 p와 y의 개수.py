def solution(s):
    pcnt,ycnt =0,0
    s=s.lower()
    for i in s:
        if i=='p':
            pcnt+=1
        if i=='y':
            ycnt+=1
    if pcnt==ycnt:
        return True
    else:
        return False