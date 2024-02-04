#2225
#합분해
#0~n까지의 정수를 k번 더해서 합이 n 경우수
#순서다르면 다른경우, 한개 여러번 가능
#k\n
#  0  1  2  3  4  5
#1 1  1  1  1  1  1
#2 1  2  3  4  5  6
#3 1  3  6 10  15 21

#이것도 dp[i][j]=dp[i-1][j]+dp[i][j-1]
n,k=map(int,input().split())
dp=[1]*(n+1)
for _ in range(1,k):
  for j in range(1,n+1):
    dp[j]+=dp[j-1]
print(dp[n]%1000000000)
