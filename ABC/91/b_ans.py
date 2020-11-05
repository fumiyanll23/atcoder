N = int(input())
s = [str(input()) for _ in range(N)]
M = int(input())
t = [str(input()) for _ in range(M)]

ans = 0
for i in set(s):
  score = s.count(i) - t.count(i)
  if score > ans:
    ans = score
print(ans)
