def move(c):
    if c=='U':
        return 0,1
    if c=='D':
        return 0,-1
    if c=='R':
        return 1,0
    if c=='L':
        return -1,0
    
def solution(dirs):
    # dirs=['U','L','R','D','D','D','D','D','D','D','D','D','D']
    answer = 0
    visited=[]
    x,y=5,5
    for i in range(len(dirs)):
        # print(i+1," ",dirs[i],move(dirs[i]),x-5,y-5,answer)
        dx=move(dirs[i])[0]
        dy=move(dirs[i])[1]
        if 0<=x+dx<=10 and 0<=y+dy<=10:
            if (x,y,x+dx,y+dy) not in visited and (x+dx,y+dy,x,y) not in visited:
                visited.append((x,y,x+dx,y+dy))
                # print(visited)
            x+=dx
            y+=dy
        else:
            continue
    
    return len(visited)