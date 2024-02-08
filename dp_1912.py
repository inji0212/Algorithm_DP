#1912
#연속합

#n개 정수 연속된 수 선택해서 최대합
#각자리에서 본인을 포함한 연속 수열의 최대값 구하기
#각자리의 계산한 수가 각자리에서의 최대 수열이 되는게 아니라 
#마지막 max를 거쳐 최대수열을 구하는 것
# ex) 수열을 밑과 같고 n=3이었으면
# 답은 -1이 아닌 리스트의 max인 3이 된다.

n=int(input())
dp=list(map(int,input().split()))

# 1 2 3 4 5 6 7 8 9 10
# 2 1 -4 3 4 -4 6 5 -5 1
# 2 3 -1 3 7 3 9 14 9 10


for i in range(1, n):
  dp[i] = max(dp[i], dp[i - 1] + dp[i])

print(max(dp))