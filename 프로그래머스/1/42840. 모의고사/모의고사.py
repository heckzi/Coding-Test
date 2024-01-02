def solution(answers):
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    cnt1=0
    cnt2=0
    cnt3=0
    for i in range(len(answers)):
        if answers[i]==p1[i%5]:
            cnt1+=1
        if answers[i]==p2[i%8]:
            cnt2+=1
        if answers[i]==p3[i%10]:
            cnt3+=1
    answer = []
    if max(cnt1,cnt2,cnt3) ==cnt1:
        answer.append(1)
    if max(cnt1,cnt2,cnt3) ==cnt2:
        answer.append(2)
    if max(cnt1,cnt2,cnt3) ==cnt3:
        answer.append(3)
    return sorted(answer)