N = int(input())
d = [int(input()) for _ in range(N)]

cnt = [0 for _ in range(100)]
for i in d:
  cnt[i-1] += 1
ans = 0
for i in range(100):
  if cnt[i] != 0:
    ans += 1
print(ans)
