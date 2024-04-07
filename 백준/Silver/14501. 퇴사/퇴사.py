n=int(input())

day=[list(map(int,input().split())) for _ in range(n)]
#DP 풀이이다
#Top down 방식
dp=[0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+day[i][0],n+1): #범위: i번째 날에 상담했을때, 상담이 가능한 모든날짜까지
        if dp[j]<dp[i]+day[i][1]: #j날짜 하루보다 이전+i날에 상담 한게 더 크면
            dp[j]=dp[i]+day[i][1]
print(dp[-1])