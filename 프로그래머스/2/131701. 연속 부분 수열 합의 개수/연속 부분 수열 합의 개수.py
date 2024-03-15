def solution(elements):
    double_e=elements*2
    arr=set()
    for count in range(1,len(elements)+1):
        for j in range(len(elements)):
            arr.add(sum(double_e[j:j+count]))
            # print(arr)
    return len(arr)