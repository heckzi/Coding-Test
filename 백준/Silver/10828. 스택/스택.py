n=int(input())
stack=[]
order=[]
for i in range(n):
    order.append(input())

for o in order:
    # print("stack",stack)
    if o=='top':
        if stack:
            print(stack[-1])
        else:
            print('-1')
    if o=='size':
        print(len(stack))
    if o=='empty':
        if stack:
            print('0')
        else:
            print(1)
    if o=='pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    if len(o.split())==2:
        temp,n=o.split()
        if temp=='push':
            stack.append(n)