def quadtree(x,y,n,arr):
    global ans0,ans1
    temp=arr[x][y]
    same=True
    for i in range(x,x+n):
        if not same:
            break
        for j in range(y,y+n):
            if arr[i][j]!=temp:
                same=False
                break
    if same:
        if temp==0:
            ans0+=1
        if temp==1:
            ans1+=1
    else:
        n//=2
        quadtree(x,y,n,arr)
        quadtree(x,y+n,n,arr)
        quadtree(x+n,y,n,arr)
        quadtree(x+n,y+n,n,arr)
        
def solution(arr):
    n=len(arr)
    global ans0,ans1
    ans0=0
    ans1=0
    quadtree(0,0,n,arr)
    return [ans0,ans1]