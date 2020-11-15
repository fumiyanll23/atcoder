N, A, B = map(int, input().split())

ans = 0
for i in range(N+1):
  dsum = sum(list(map(int, str(i))))
  if A <= dsum <= B:
    ans += i
print(ans)
