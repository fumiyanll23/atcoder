N = int(input())
p = list(map(int, input().split()))

ans = 0
start = 0
for i in range(N):
  if p[i] != ans:
    print(ans)
  else:
    ans += 1
    for j in range(start, i):
      if p[j] == ans:
        ans += 1
        j = 0
    print(ans)