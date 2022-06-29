N, K, M = map(int, input().split())
A = list(map(int, input().split()))

diff = N*M - sum(A)
if diff <= K and diff < 0:
  print(0)
elif diff <= K and diff >= 0:
  print(diff)  
else:
  print(-1)