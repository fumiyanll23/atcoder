N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
A, B = 0, 0
for i in range(N):
  if i%2 == 0:
    A += a[i]
  else:
    B += a[i]
print(A - B)
