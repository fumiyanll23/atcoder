N = int(input())
A = list(map(int, input().split()))

sub= [0 for i in range(N)] # Number of sub of No. i
for i in range(N-1):
  for j in range(N):
    if(A[i]-1 == j):
      sub[j] += 1
for i in range(N):
  print(sub[i])

# TLE & WA