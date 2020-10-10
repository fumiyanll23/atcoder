N = int(input())
p = list(map(int, input().split()))

appear = [0 for _ in range(200001)]
ans = 0
for i in p:
  appear[i] = 1
  while appear[ans]:
    ans += 1
  print(ans)