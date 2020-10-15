N, A, B = map(int, input().split())

ans = 0
for i in range(N+1):
  ds = sum(list(map(int, str(i))))
  if A<=ds and ds<=B:
    ans += i
print(ans)
