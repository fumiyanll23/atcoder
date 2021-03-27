N, M, X = map(int, input().split())
A = list(map(int, input().split()))

lower = 0
upper = 0
for i in A:
  if i < X:
    lower += 1
  else:
    upper += 1
print(min(lower, upper))
