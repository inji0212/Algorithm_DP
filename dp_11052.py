#11052
# 카드구매하기

# 8가지 등급 가격 p
# i개는 pi원의 리스트 조합중 n개를 고를 수 있는 최대
# n개보다 ㅏㄴㅎ은 팩을 사서 버리는 거슨 안된다.
# 1 5 6 7 - 10 4
# 1
# 1 1,5
# 1 1 ,5 1,
# 1111,5 5, 6 1,7
#dp[i-1]+p[0],p[i]
n=int(input())

p=list(map(int,input().split()))

d=[0]
dp=d+p
dp[1]=p[0]
for i in range(1,n+1):
  for j in range(1,i+1):
    dp[i]=max(dp[i],dp[i-j]+dp[j])
print(dp[n])