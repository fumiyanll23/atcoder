N = int(input())
P = list(map(int, input().split()))

flag = [1 for i in range(N)]
for i in range(1, N):
  for j in range(i):
    if P[i] > P[j]:
      flag[i] = 0
print(sum(flag))