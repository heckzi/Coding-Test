import numpy as np
def solution(arr1, arr2):
    n1=np.array(arr1)
    n2=np.array(arr2)
    answer=(n1@n2).tolist()
    
    return answer