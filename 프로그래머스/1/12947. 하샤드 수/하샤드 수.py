def solution(x):
    sx=list(str(x))
    # print(sx)
    sum=0
    sx=list(map(int,sx))
    # print(type(sx[0]))
    for i in sx:
        sum+=i
    if x%sum==0:
        return True
    else:
        return False
