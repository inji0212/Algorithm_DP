# 9625
# babba
# 버튼 누르니 a가 b로 변함 
# 한번 더 누르면 ba , 그담 bab, 그담 babba
# 모든 b 는 ba 로 a 는 b로 바뀐다.
# k번 누를 때 a,b 개수
# a,b,ba,bab,babba,babbabab,babbababbabba,
# 1 2 2+1,3+2,4+3,5+4,6+5
# 1=>a
# 2=>b
# 3=> 2+1
# [i]=[i-1] +[i-2]

#a,b 갯수로 보면
#1 0, 0 1,1 1,1 2,2 3,3 5,5 8,...
# a는 b 가 있어야 생성이 되어서
# a[i]= i-1번째 b의 개수
# b는 a와 b모두 생성하므로 
# b[i]= i-1번째 길이

# 메모리 초과되기에 개수세는 리스트로
n=int(input())
data=[0]*(n+1)

data[1]=1
for i in range(2,n+1):
  data[i]=data[i-1]+data[i-2]

if n==0:
  print(1,0)
else:
  print(data[n-1],data[n])