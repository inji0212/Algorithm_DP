#2293
#동전1
#n개 종류 합이 k가 되는 경우수 동전 중복가능
#순서달라도 같은 경우

n,k=map(int,input().split())
coin=[]
for _ in range(n):
  coin.append(int(input()))

coin.sort()
#3 10
#1 2 5
# 1-1 1
# 2-2 11,2
# 3-2 111,12
# 4-3 1111,112,22
# 5-4 11111,1112,122,5
# 6-5 1 6개,11112,1122,222,15
# 7-6   1 7개,111112,11122,1222,115,25
# 8-7 1 8개, 1111112,111122,11222,2222,1115,125
#9-8 19개,17개2,15개22,111222,12222,11115,1125,225
#10-10 110개,111111112,11111122,1111222,112222,22222,111115,11125,1225,55

#k원의 배수만큼 기회가 생기나?

#  1 2 3 4 5 6 7 8 9 10
#1 1 1 1 1 1 1 1 1 1  1
#2 0 1 1 2 2 3 3 4 4  5
#5 0 0 0 0 1 1 2 2 3  4
#총 1 2 2 3 4 5 6 7 8 10

# if coin[j]<i,dp[i]+=dp[i-coin[j]]
#찾기 드릅게으렵네
dp=[0]*(k+1)  
dp[0]=1
for i in coin:
  for j in range(i,k+1):
    dp[j]+=dp[j-i]
#    1 2 3 4 5 6 7 8 9 10 
#1=> 1 1 1 1 1 1 1 1 1 1
#2=> 1 2 2 3 3 4 4 5 5 6
#5=> 1 2 2 3 4 4 6 7 8 10
print(dp[k])