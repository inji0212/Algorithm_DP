#11057
#오르막수

#오름차순, 인접수가 같아도 오름차순
#0~9숫자들로 조합된 오르막 수

#n\끝숫자
#  0 1 2  3  4  5  6  7  8  9
#1 1 1 1  1  1  1  1  1  1  1  -10
#2 1 2 3  4  5  6  7  8  9 10  -55
#3 1 3 6 10 15 21 28 36 45 55 -220

# dp[i][j]=dp[i][j-1]+dp[i-1][j]
# 를 1차원으로 표현하면
n=int(input())
dp=[1]*10
for _ in range(1,n):
 for j in range(1,10):
   dp[j]+=dp[j-1]
   #dp[i][j-1]는 j-1에서 더해주고
   #dp[i-1][j]은 dp[j]가 아직 변하지 않아 
   #dp[j]에 같은 값이 들어있다.

print(sum(dp)%10007)