#2579
#계단오르기
# 한번에 한개 혹은 두개 가능
# ㅕㄴ속 세개는 안된다. # 시작은 0
# 마지마 도착계단은 밟아야함
#10
#20
#15
#25
#10
#20

n=int (input())
stairs=[0]*(n+1)
for i in range(1,n+1):
  stairs[i]=int(input())

# 1계단 오르려면 3계단전에 2계단 오르고 1계단
# 2계단 오르려면 그냥2계단
# dp[i-3]+stairs[i-1]
# dp[i-2]
dp=[0]*(n+1)
for i in range (1,n+1):
  if i<=2:
    dp[i]=dp[i-1]+stairs[i]
  else:
    dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])
print(dp[n])