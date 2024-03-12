def left_rotate(s,n):
    r=[None]*len(s)
    for i in range(len(s)):
        r[i-n]=s[i]
    return r
def solution(s):
    answer = 0
    temp=[]
    ok=True
    for l in range(0,len(s)):
        rs=left_rotate(s,l)
        temp=[]
        ok=True
        # print("rs",rs)
        for i in rs:
            if i=='[' or i=='{' or i =='(':
                temp.append(i)
            if i==']':
                if temp:
                    if '[' in temp:
                        temp.pop()
                    else:
                        ok=False
                        break
                else:
                    ok=False
                    break 
            if i=='}':
                if temp:
                    if '{' in temp:
                        temp.pop()
                    else:
                        ok=False
                        break
                else:
                    ok=False
                    break 
            if i==')':
                if temp:
                    if '(' in temp:
                        temp.pop()
                    else:
                        ok=False
                        break
                else:
                    ok=False
                    break 
        if temp:
            ok=False
        if ok:
            answer+=1
        # print(ok,temp)
    return answer