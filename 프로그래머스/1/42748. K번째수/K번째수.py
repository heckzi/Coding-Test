def solution(array, commands):
    answer = []
    for i in range (len (commands)): 
        arr1 = array[commands[i][0]-1:commands[i][1]]
        answer.append(sorted(arr1)[commands[i][2]-1])
    return answer