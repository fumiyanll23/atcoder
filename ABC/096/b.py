a = list(map(int, input().split()))
K = int(input())

for _ in range(K):
  a.sort(reverse=True)
  a[0] *= 2
print(sum(a))
