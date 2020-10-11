N, M = map(int, input().split())
w = list(map(int, input().split()))
l = [0 for _ in range(M)]
v = [0 for _ in range(M)]
for i in range(M):
  l[i], v[i] = map(int, input().split())

if min(w) > max(v):
  print(-1)
  exit()
