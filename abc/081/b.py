N = int(input())
A = list(map(int, input().split()))

cnt = [0 for _ in range(N)]
for i in range(N):
  while A[i]%2 == 0:
    A[i] //= 2
    cnt[i] += 1
print(min(cnt))
