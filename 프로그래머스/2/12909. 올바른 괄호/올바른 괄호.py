# def solution(s):
#     answer = True
#     cnt1=0
#     cnt2=0
#     sp = list(s)
#     for i in sp:
#         if i == '(': # '('일 때
#             cnt1+=1
#             if cnt2!=0: #새로 열렸는데 )가 남아있으면
#                 answer = False
#                 break
#         if i == ')': # ')'일 때
#             cnt2+=1 
#             if cnt1==0: # 열린게 없는데 닫으면
#                 answer = False
#                 break
#             if cnt1!=0: #열린게 있을 때
#                 if cnt1==cnt2: # 갯수가 맞을때
#                     cnt1=0 #초기화
#                     cnt2=0
#     return answer
def solution(s):
    stack=[]
    for i in s:
        if i =='(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else: 
        return False