# 1932
# 정수 삼각형
# 위에서 아래로 수 합 최대인 경로 인접으로만 이동

n=int(input())
dp=[[0*(n)]]*(n)
for i in range(n):
  dp[i]=list(map(int,input().split()))

# 각 자리에 최대경우를 넣기?
# i-1,i비교 if 0,0 if n,n-1
#7 0
#3 8-1 
#8 1 0-2
#2 7 4 4 -3 
#4 5 2 6 5

for i in range(1,n):
  for j in range(0,i+1):
    if j==0: 
      dp[i][j]+=dp[i-1][j]
    elif j==i:
      dp[i][j]+=dp[i-1][j-1]
    else:
      dp[i][j]+=max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[n-1]))
      