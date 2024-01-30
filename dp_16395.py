#16395
#파스칼의 삼각형
#n번째 n개
# 첫번째 행1 두번째행부터 행 양끝1 
# 나머지 스는 바로 위 인접한 두수의 합
#n[i]=n-1[i-1]+n-1[i]

n ,k = map(int,input().split())
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,i+1):
    if j==1 or j==i:
      dp[i][j]=1
    else:
      dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

print(dp[n][k])
  