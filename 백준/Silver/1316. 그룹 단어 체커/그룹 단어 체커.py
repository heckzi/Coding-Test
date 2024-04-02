n=int(input())
words=[]
for i in range(n):
    words.append(input())

answer=0
for w in words:
    stack=[]
    stop=False
    temp=list(w)
    for a in temp:
        if a not in stack:
            stack.append(a)
        if a in stack:
            if a!=stack[-1]:
                stop=True
                break
            else:
                continue
    if not stop:
        answer+=1
print(answer)