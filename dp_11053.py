#11053
#가장 긴 증가하는 부분수열
#LIS
# 10,20,10,30,20,50 중
# 10,20,30,,50이고 길이 4

n=int(input())
dp=[]
dp=list(map(int,input().split()))
# 길이 구하는 문제
# 각 자리마다
#dp[i]<dp[k]일 시 
# 순서대로 일 수도 있고 아닐수도 있음
# ...i,k가 답이라고 생각하면 i번쨰 길이 +1 이랑 
# i나오기전 길이 즉 현재까지의k의 길이랑 비교
#(순서대로가 아니면 i추가 안하게 더클 수도
# 혹은 i까지의 수열이 더 클 수도 있기에)
# max(length[k],length[i]+1)
length=[0]*n
for k in range(n):
  length[k]=1
  for i in range(k):
    if dp[k]>dp[i]:
      length[k]=max(length[k],length[i]+1)
print(max(length))

