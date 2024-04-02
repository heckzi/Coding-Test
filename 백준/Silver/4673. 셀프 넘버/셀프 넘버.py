def is_self(n):
    nlist=list(str(n))
    # print(nlist)
    sum=0
    sum+=n
    for num in nlist:
        sum+=int(num)
    return sum
nomi=[]
for i in range(0,10000):
    if is_self(i) <=10000:
        nomi.append(is_self(i))
for j in range(1,10000):
    if j not in nomi:
        print(j)