# ABC177-C
N = int(input())
A = list(map(int, input().split()))
i = 0
j = i + 1
s = 0

for i in range(N-1):
  for j in range(N):
    s += A[i] * A[j]
    
s %= 10**9 + 7
print(s)