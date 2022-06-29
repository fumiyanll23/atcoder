K, N = map(int, input().split())
A = list(map(int, input().split()))

d = [0 for i in range(N-1)]
for i in range(N-1):
  d[i] = A[i+1] - A[i] # Input each distance except the last (first) house
d[N-2] = A[0] + K - A[N-1] # The last (first) house

flag = [0 for i in range(N)]
ans = 0
while(sum(flag) != N-1): # The last house is obvious