N, M, K = map(int, input().split())
A = map(int, input().split)
B = map(int, input().split)

time = 0
book = 0
while(time < K):
  if(A[i] >= B[i]):
    time += B[i]
    book += 1
  else:
    time += A[i]
    book += 1
