x=int(input())
y=int(input())
global a
if x>0:
    if y>0:
        a=1
    else:
        a=4
if x<0:
    if y>0:
        a=2
    else:
        a=3
print(a)