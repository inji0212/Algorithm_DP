#12865
#평범한 배낭
#n개 물건 w무게 v가치 최대k무게

n,k = map(int,input().split())
data=[]
for _ in range(1,n+1):
  a,b=map(int,input().split())
  data.append((a,b))

dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
#최대k무게까지의 가치
#4 7
#6 13
#4 8
#3 6
#5 12
# 경우\최대무게
#      1  2  3  4  5  6  7
#6,13  0  0  0  0  0 13 13
#4,8   0  0  0  8  8 13 13
#3,6   0  0  6  8  8 13 14
#5,12  0  0  6  8 12 13 14
# dp[i][j] j<data[i][0]=>기존 데이터
# dp[i][j] j>=data[i][0]=>max 비교
# 기존dp(dp[i-1][j]) ,data[i][1]에 더할 수 있는 max비교
# 즉 dp[i][j]+data[i][1]에서 j는 
# j-data[i][0]]

for i in range(1,n+1):
  for j in range(1,k+1):
    if j<data[i-1][0]:
      dp[i][j]=dp[i-1][j]
    else:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-data[i-1][0]]+data[i-1][1])

print(dp[n][k])