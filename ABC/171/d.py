N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B, C = map(int, input().split())

A = sorted(A) # probably faster if add "break"
for i in range(Q):
  for j in range(N):
    if(A[j] == B[i]):
      A[j] = C[i]