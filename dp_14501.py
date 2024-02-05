#14501
#퇴사
#n+1일차에 퇴사
#숫자를 넘기거나 일중이면 상담X
#얻을 수 있는 최대 수익

n=int(input())
t=[0]
p=[0]
for _ in range(n):
  a,b=map(int,input().split())
  t.append(a)
  p.append(b)

# 1일까지 최대 돈 0
# 2일까지 최대 돈 0
# 3일까지 최대 돈 5-1
# 4일까지 최대 돈 30-1,4
# 5일까지 최대 돈 30-1,4
# 6일까지 최대 돈 30-1,4
#(5일차랑 6일차로 만들수 있는거 최대)
# 7일까지 최대 돈 45-1,4,5

dp=[0]*(n+2)
# for문을 돌리면 10에서 하루 더 일할 수도 있기에
#n+1일까지 자리가 있어야한다.

#1~n까지
# i일까지+i일부터 걸린 시간의 비용이 
# 이후의 비용보다 크면 i의 최대+p[i]가 가장 클수 밖에
# 그날은 현재가격에서 변동 될 일이없어서 저장
# 을 반복하면 전체적으로 검사가 된다.
for i in range(n+1):
  for j in range(i+t[i],n+2):
    if dp[j]<dp[i]+p[i]:
      # i까지 최대값+i일의 수익
      dp[j]=dp[i]+p[i]
  print(i,dp)

print(dp)