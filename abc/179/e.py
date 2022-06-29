N, X, M = map(int, input().split())

A = [0 for i in range(N)]
A[0] = X
for i in range(N-1):
  A[i+1] = (A[i]**2) % M
print(sum(A))