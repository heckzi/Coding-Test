# from collections import deque
# def binary_s(array,target,start,end):
#     while(start<=end):
#         mid=(start+end)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]>target:
#             end=mid-1
#         elif array[mid]<target:
#             start=mid+1
#         return None
        
    
# def solution(order):
#     answer = 0
#     order=deque(order)
#     box=[i for i in range(1,1000001)]
#     box=deque(box)
#     stack=deque()
#     while order:
#         if box[0]==order[0]:
#             box.popleft()
#             order.popleft()
#             answer+=1
#         elif stack and stack[-1]==order[0]:
#             stack.pop()
#             order.popleft()
#             answer+=1
#         elif stack and binary_s(stack,order[0],0,len(stack)-1) is not None and order[0]!=stack[-1]:
#             break
#         else:
#             stack.append(box.popleft())
#         # print(order,stack,box,answer)
#     return answer
from collections import deque

def solution(order):
    answer = 0
    order = deque(order)
    box = deque(range(1, 1000001))
    stack = deque()
    while order:
        if box and box[0] == order[0]:
            box.popleft()
            order.popleft()
            answer += 1
        elif stack and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            answer += 1
        elif stack and order[0] < stack[-1]:
            return answer  # 스택에 이미 쌓인 값보다 작은 값을 추가하려 하므로 불가능한 경우
        else:
            while box and box[0] != order[0]:
                stack.append(box.popleft())
            if not box:
                return answer  # 더 이상 상자에 값이 없는데 주문이 남아있는 경우
    return answer