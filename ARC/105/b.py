N = int(input())
a = list(map(int, input().split()))

X = max(a)
x = min(a)
while X != x:
  a.sort(reverse=True)
  for i in range(N):
    if a[i] == X:
      a[i] = X - x
    else:
      break
  X = max(a)
  x = a[N-1]
print(a[0])
