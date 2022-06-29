A, B, K = map(int, input().split())

if (B-A+1) <= K*2:
  for i in range(B-A+1):
    print(A+i)
else:
  for i in range(K):
    print(A+i)
  for i in range(K):
    print(B-K+1+i)
