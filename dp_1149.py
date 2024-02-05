#1149
#rgb거리
# 집 n개 빨 초 파 하나의 색
#1!=2,n!=n-1 i-1!=i!=i+1
#즉 인접한 집 같은색X
n=int(input())
dp=[[0]*3]*(n+1)
for i in range(1,n+1):
  dp[i]=list(map(int,input().split()))

# dp[i-1]+가능최소 ,dp[i]가능 최소에다른경우?
# ㄴㄴ

#각자리에서의 최소값을?
#dp[i]에서 0일때 1일때 2일때 최소값넣고 
#0일때는 [i-1]의1,2 ...
cost=[0]*(n+1)
for i in range(1,n+1):
  dp[i][0]+=min(dp[i-1][1],dp[i-1][2])
  dp[i][1]+=min(dp[i-1][0],dp[i-1][2])
  dp[i][2]+=min(dp[i-1][0],dp[i-1][1])
  #dp에 각자리경우일때의 최소값들어가고
  cost[i]=min(dp[i])
  
print(cost[n])