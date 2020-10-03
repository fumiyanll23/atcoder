n, S = map(str, input().split())
N = int(n)

ans = 0
for i in range(N):
  at, cg = 0, 0
  for j in range(i, N):
    if S[j] == 'A':
      at += 1
    elif S[j] == 'T':
      at -= 1
    elif S[j] == 'C':
      cg += 1
    else:
      cg -= 1
    if at==0 and cg==0:
      ans += 1
print(ans)

### Why are U 'TLE'??