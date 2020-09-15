N = int(input())
X = list(map(int, input().split()))

X = sorted(X)
d = [0 for i in range(N)]
for i in range(1, max(X)):
  for j in range(N):
    d[j] = (X[j]-i) ** 2
print(min(d))