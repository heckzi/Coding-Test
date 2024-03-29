def solution(n, arr1, arr2):
    answer = []
    map1=[]
    map2=[]
    for i in range(n):
        map1.append(list(format(arr1[i],'0'+str(n)+'b')))
        map2.append(list(format(arr2[i],'0'+str(n)+'b')))
    for a in range(n):
        for b in range(n):
            map1[a][b]=int(map1[a][b])+int(map2[a][b])
            if map1[a][b]==2:
                map1[a][b]=1
            if map1[a][b]==1:
                map1[a][b]='#'
            if map1[a][b]==0:
                map1[a][b]=' '
    for final in range(n):
        answer.append(''.join(map1[final]))
    return answer