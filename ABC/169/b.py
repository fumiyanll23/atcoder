N = int(input())
A = list(map(int, input().split()))

prd = 1
for i in range(N):
  prd *= A[i]
if(prd > 10**18):
  print(-1)
else:
  print(prd)

# Why printed TLE??