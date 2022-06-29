N = int(input())
x = [0 for i in range(N)]
y = [0 for i in range(N)]
for i in range(N):
  x[i], y[i] = map(int, input().split())

d = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
  for j in range(N):
    if i < j:
      d[i][j] = abs(x[i]-x[j]) + abs(y[i]-y[j])
print(max(max(d)))

# As you know, returned "TLE"...