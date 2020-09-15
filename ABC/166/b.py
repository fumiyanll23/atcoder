N, K = map(int, input().split())

for i in range(K):
  d[i] = int(input())
  for j in range(d[i]):
    A[i][j] = map(int, input().split())
# What's called "内包表記" ??