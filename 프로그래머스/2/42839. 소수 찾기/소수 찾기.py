from itertools import permutations
import math
def is_prime(n): #에라토스테네스의 체
    for i in range(2,int(math.sqrt(n))+1): #sqrt까지만 나눠봐도 알 수 있다.
        if n%i==0:
            return False
    return True
def solution(numbers):
    list_n = sorted(list(numbers))
    answer = 0
    str=[]
    final_list=[]
    for i in range(len(list_n)):
        per_list = list(permutations(list_n,i+1))
        for j in range(len(per_list)):
            str="".join(per_list[j])
            final_list.append(int(str)) #int형으로 바꿔서 011 => 11로 추가하기
    final_list=list(set(final_list)) # 중복제거
    for fl in final_list:
        if is_prime(fl) and fl >1: #2이상부터 검사
            answer+=1
    return answer
